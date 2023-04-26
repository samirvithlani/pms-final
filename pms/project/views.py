from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from .models import *
from . models import Projet_team
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return redirect('/user/login')

class ProjectCreationView(CreateView):
    form_class =ProjectCreationForm
    model = Project
    template_name = 'project/project_create.html'
    success_url = '/project/list_project/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'project_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by', 'title')
        sort_by = self.request.GET.get('sort_by', 'technology')
        direction = self.request.GET.get('direction', 'asc')
        if direction == 'asc':
            queryset = queryset.order_by(sort_by)
        elif direction == 'desc':
            queryset = queryset.order_by(f'-{sort_by}')
        return queryset    
    

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/project/list_project/'
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project_detail'

    labels=[]
    data =[]
    project = Project.objects.all().values_list('title',flat=True)
    time = Project.objects.all().values_list('estimatedHours',flat=True)
    for i in project:
        labels.append(i)
    for i in time:
        data.append(i)
    
    def get(self, request, *args, **kwargs):
         team = Projet_team.objects.filter(project_id =self.kwargs['pk'])
         module = Project_module.objects.filter(project_id=self.kwargs['pk'])
         return render(request, self.template_name, {'project_detail': self.get_object(),'team':team,'module':module,'labels':self.labels,'data':self.data})
    
      
    
class ProjectDeleteView(DeleteView):
    model = Project
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/list_project/'    
    
class Create_Project_team(CreateView):
    form_class =ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/project/list_project/'

class ProjectTeamListView(ListView):
    model = Projet_team
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
class ProjectTeamByProject(ListView):
    model = Projet_team
    template_name = 'project/projectteam_list.html'
    context_object_name = 'project_team_list'
    
    def get_queryset(self):
        return super().get_queryset().filter(project_id=self.kwargs['pk'])
    
class CreateProjectModule(CreateView):
    model = Project_module
    form_class = CreateProjectModuleForm
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/'
    
        

class ProjectModuleListByProject(ListView):
    model = Project_module
    template_name = 'project/project_module_list.html'
    context_object_name = 'project_module_list'
    
    
   # def get_queryset(self):
       # return super().get_queryset().filter(project_id=self.kwargs['pk'])

class ModuleUpdateView(UpdateView):
    model = Project_module
    form_class = CreateProjectModuleForm
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/' 
    
class ModuleDeleteView(DeleteView):
    model = Project_module
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/list_project_module/'

class TeamDeleteView(DeleteView):
    model = Projet_team
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/detail_project /'

class CreateProjectTask(CreateView):
    model = Task
    form_class = CreateProjectTaskForm
    template_name = 'project/project_task_create.html'
    success_url = '/project/list_project_task/'

class ProjectTaskListByProject(ListView):
    model = Task
    template_name = 'project/project_task_list.html'
    context_object_name = 'project_task_list'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = CreateProjectTaskForm
    template_name = 'project/project_task_create.html'
    success_url = '/project/list_project_task/' 
    
class TaskDeleteView(DeleteView):
    model = Task
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/list_project_task/'

class AssignProjectTask(CreateView):
    form_class = AssignProjectTaskForm
    template_name = 'project/project_task_assign.html'
    success_url = '/project/assign_project_task/' 

class ProjectTaskListView(ListView):
    model = user_task
    template_name = 'project/project_task_list_assign.html'
    context_object_name = 'project_task_list_assign'


