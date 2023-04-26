from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('create_project/',ProjectCreationView.as_view(),name='create_project'),
    path('list_project/',ProjectListView.as_view(),name='project_list'),
    path('delete_project/<int:pk>',ProjectDeleteView.as_view(),name='delete_project'),
    path('update_project/<int:pk>',ProjectUpdateView.as_view(),name='update_project'),
    path('detail_project/<int:pk>',ProjectDetailView.as_view(),name='detail_project'),

    path('create_project_team/',Create_Project_team.as_view(),name='create_project_team'),
    path('list_project_team/',ProjectTeamListView.as_view(),name='project_team_list'),
    path('list_project_team1/<int:pk>',ProjectTeamByProject.as_view(),name='project_team_list1'),

    path('create_project_module/',CreateProjectModule.as_view(),name='create_project_module'),
    path('list_project_module/<int:pk>',ProjectModuleListByProject.as_view(),name='project_module_list'),
    path('list_project_module/',ProjectModuleListByProject.as_view(),name='project_module_list'),
    path('delete_module/<int:pk>',ModuleDeleteView.as_view(),name='delete_module'),
    path('update_module/<int:pk>',ModuleUpdateView.as_view(),name='update_module'),

    #path('detail_project/<int:pk>',ProjectDetailView.as_view(),name='detail_project'),

    path('delete_team/<int:pk>',TeamDeleteView.as_view(),name='delete_team'),

    path('create_project_task/',CreateProjectTask.as_view(),name='create_project_task'),
    path('list_project_task/<int:pk>',ProjectTaskListByProject.as_view(),name='projectask_list'),
    path('list_project_task/',ProjectTaskListByProject.as_view(),name='projectask_list'),
    path('delete_task/<int:pk>',TaskDeleteView.as_view(),name='delete_task'),
    path('update_task/<int:pk>',TaskUpdateView.as_view(),name='update_task'),
    
    path('assign_task/<int:pk>',AssignProjectTask.as_view(),name='assign_task'),
    path('assign_project_task/',ProjectTaskListView.as_view(),name='assign_project_task'),
]

