from django.shortcuts import render,redirect
from django.views.generic import View
from ToDo_App.forms import register,sign_in,Task_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from ToDo_App.models import Task
from django.utils.decorators import method_decorator
from django.contrib import messages


# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"You Should Login First...")
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def mylogin(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Task.objects.get(id=id)
        if obj.user!=request.user:
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

# regiter page
class signup_view(View):
    def get(self,request,*args,**kwargs):
        form=register()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print(form.cleaned_data)
        form=register() 
        return redirect('login')

# login page
    
class signin_view(View):
    def get(self,request,*args,**kwargs):
        form=sign_in()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=sign_in(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(u_name,pwd)
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                print("valid credential")
                login(request,user_obj)
                return redirect('task')
            else:
                print("invalid credential")
            return render(request,"signin.html",{"form":form})

@method_decorator(signin_required,name='dispatch') 
class Task_view(View):
    def get(self,request,*args,**kwargs):
        form=Task_form()
        data=Task.objects.filter(user=request.user).order_by('complete')
        return render(request,"task.html",{"form":form,"data":data})
    def post(self,request,*args,**kwargs):
        form=Task_form(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        data=Task.objects.filter(user=request.user)
        return render(request,"task.html",{"form":form,"data":data})

class signout_view(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
    
class task_edit(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        edit=Task.objects.get(id=id)
        if edit.complete == False:
            edit.complete = True
            edit.save()
        elif edit.complete == True:
            edit.complete = False
            edit.save()
        return redirect('task')


@method_decorator(signin_required,name='dispatch')
@method_decorator(mylogin,name='dispatch')

class task_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.filter(id=id).delete()
        return redirect('task')

class user_del(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        User.objects.get(id=id).delete()
        return redirect('reg')

        
