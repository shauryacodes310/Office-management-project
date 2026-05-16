from django import forms

from .models import Project

from accounts.models import User


class ProjectForm(forms.ModelForm):

    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:

        model = Project

        fields = [
            'name',
            'description',
            'members',
        ]