from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView,DeveloperRegisterView,UserLoginView,UserLogoutView,SignUpView
from . import views
from .views import *
# from django.contrib.auth.views import LogoutView
urlpatterns = [
 
 path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
 path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
 path('login/',UserLoginView.as_view(),name='login'),
 path('logout/',UserLogoutView.as_view(),name='logout'),
 path('signup/',SignUpView.as_view(),name='signup'),
 path('dashboard/',views.dashboard,name='dashboard'),
 path('password/',views.password,name='password'),
 path('manager/dashboard/',ManagerDashboardView.as_view(),name='manager_dashboard'),
 path('developer/dashboard/',DeveloperDashBoardView.as_view(),name='developer_dashboard'),
 path('detail_task/<int:pk>',TaskDetailView.as_view(),name='detail_task'),
 path('detail_task/',TaskDetailView.as_view(),name='detail_task'),
 path('task_board/',TaskBoardView.as_view(),name='task_board'),

]
