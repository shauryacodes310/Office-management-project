from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Task

from .forms import TaskForm

from accounts.decorators import admin_required


@login_required
def task_list(request):

    if request.user.role == 'admin' or request.user.is_superuser:

        tasks = Task.objects.all()

    else:

        tasks = Task.objects.filter(
            assigned_to=request.user
        )

    return render(request, 'tasks/task_list.html', {

        'tasks': tasks
    })


@login_required
@admin_required
def create_task(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.created_by = request.user

            task.save()

            return redirect('task_list')

    else:

        form = TaskForm()

    return render(request, 'tasks/create_task.html', {

        'form': form
    })


@login_required
def update_task_status(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    if request.method == 'POST':

        new_status = request.POST.get('status')

        task.status = new_status

        task.save()

    return render(
        request,
        'tasks/partials/task_row.html',
        {
            'task': task
        }
    )   