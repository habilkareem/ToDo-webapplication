from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from django.contrib.auth.models import User
from works.forms import RegisterForm,LoginForm,ProjectaddingForm,TodoaddingForm
from django.contrib.auth import authenticate,login,logout
from works.models import Project,Todo

# Create your views here.

#Registration View

class Register(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,"works/register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            form=RegisterForm()
            return redirect("login")
        
#Login View

class Login(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"works/login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("projectadd")
            else:
                return render(request,"works/login.html",{"form":form})
            

class ProjectaddingView(View):
    def get(self,request,*args,**kwargs):
        form=ProjectaddingForm()
        return render(request,"works/projectadding.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=ProjectaddingForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            form=ProjectaddingForm()
        return render(request,"works/projectadding.html",{"form":form})
    
class ProjectlistView(View):
    def get(self,request,*args,**kwargs):
        data=Project.objects.filter(user=request.user)
        return render(request,"works/projectlist.html",{"data":data})
    
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("register")
    
class DeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Project.objects.get(id=id).delete()
        return redirect("projectlist")
    
class UpdateView(View):
    def get(self,request,*args,**kwargs):
        k=kwargs.get("pk")
        res=Project.objects.get(id=k)
        form=ProjectaddingForm(instance=res)
        return render(request,"works/projectedit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        k=kwargs.get("pk")
        res=Project.objects.get(id=k)
        form=ProjectaddingForm(request.POST,instance=res)
        if form.is_valid():
            form.save()
            return redirect("projectlist")
        else:
            return render(request,"works/projectedit.html",{"form":form})
        
# project views end----------------------------------------------------------------------

# class TodoaddingView(View):
#     def get(self,request,*args,**Kwargs):
#         form=TodoaddingForm()
#         return render(request,"works/todoadding.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form=TodoaddingForm(request.POST)
#         if form.is_valid():
#             Todo.objects.create(**form.cleaned_data)
#             form=TodoaddingForm()
#             return render(request,"works/project_todo.html",{"form":form})
#         else:
#             return render(request,"works/project_todo.html",{"form":form})

class ProjectTodoView(View):
    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        todos = Todo.objects.filter(project=project)
        form = TodoaddingForm()  # Instantiate an empty TodoForm

        return render(request, 'works/project_todo.html', {'project': project, 'todos': todos, 'form': form})

    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = TodoaddingForm(request.POST)

        if form.is_valid():
            # Create a new Todo instance and associate it with the project
            todo = form.save(commit=False)
            todo.project = project
            todo.save()
            return redirect('project_todo', project_id=project_id)
        else:
            # Form is not valid, re-render the page with errors
            todos = Todo.objects.filter(project=project)
            return render(request, 'works/project_todo.html', {'project': project, 'todos': todos, 'form': form})

class TodoUpdateView(View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        form = TodoaddingForm(instance=todo)
        return render(request, 'works/todo_update.html', {'form': form})

    def post(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        form = TodoaddingForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('project_todo', project_id=todo.project.id)
        return render(request, 'works/todo_update.html', {'form': form})

class TodoDeleteView(View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return redirect('project_todo', project_id=todo.project.id)

