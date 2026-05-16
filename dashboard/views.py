from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tasks.models import Task


@login_required
def dashboard(request):

    tasks = Task.objects.all()

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(status='done').count()

    pending_tasks = tasks.exclude(status='done').count()

    overdue_tasks = tasks.exclude(
        status='done'
    ).filter(
        due_date__lt='2026-05-16'
    ).count()

    return render(request, 'dashboard/dashboard.html', {

        'total_tasks': total_tasks,

        'completed_tasks': completed_tasks,

        'pending_tasks': pending_tasks,

        'overdue_tasks': overdue_tasks,

        'tasks': tasks,
    })