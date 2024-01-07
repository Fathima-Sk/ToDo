"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ToDo_App.views import signup_view,signin_view,signout_view,Task_view,task_edit,task_delete,user_del

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',signup_view.as_view(),name='signup'),
    path('',signin_view.as_view(),name="login"),
    path('task/',Task_view.as_view(),name='task'),
    path('task/edit/<int:pk>',task_edit.as_view(),name="edit"),
    path('task/remove/<int:pk>',task_delete.as_view(),name="remove"),
    path('signout/',signout_view.as_view(),name='logout'),
    path('del/<int:pk>',user_del.as_view())
]
