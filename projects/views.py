from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Project

from .forms import ProjectForm

from accounts.decorators import admin_required


@login_required
def project_list(request):

    if request.user.role == 'admin':

        projects = Project.objects.all()

    else:

        projects = Project.objects.filter(
            members=request.user
        )

    return render(request, 'projects/project_list.html', {

        'projects': projects
    })


@login_required
def project_detail(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    return render(request, 'projects/project_detail.html', {

        'project': project
    })


@login_required
@admin_required
def create_project(request):

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.created_by = request.user

            project.save()

            form.save_m2m()

            return redirect('project_list')

    else:

        form = ProjectForm()

    return render(request, 'projects/create_project.html', {

        'form': form
    })