from django import forms
from .models import *
from user.models import User

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model =Project
        fields ='__all__'
        
    

class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))
    
    class Meta:
        model =Projet_team
        fields ='__all__'

class CreateProjectModuleForm(forms.ModelForm):
    class Meta:
        model = Project_module
        fields = '__all__'     

class CreateProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__' 

class CreateProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'    

class AssignProjectTaskForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))

    class Meta:
        model = user_task
        fields = '__all__'