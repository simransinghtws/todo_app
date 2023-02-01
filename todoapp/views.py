from turtle import up
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todoapp.models import User,Todo
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        repassw=request.POST.get('password2')
        if User.objects.filter(username=name).exists():
            messages.warning(request, 'User Already Exists')
            return render(request,'login.html')
                           
        else:
            if len(passw)>=8:
                if passw==repassw:
                    User.objects.create_user(username = name , email = email  , password = passw)
                    return render(request,'login.html') 
                    
                else:
                    messages.error(request, 'Password Not Match')
                    
            else:
                messages.error(request, 'Password contains only more then 8 characters')
            
    return render(request,'signup.html')

def login_form(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username, password)
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Login Successful')
                return redirect('home')

            else:
                messages.error(request, 'please Signup')
                return render(request,'login.html')
        else:
            return render(request,'login.html')

@login_required
def logout_form(request):
    logout(request)
    return redirect('login_form')
    

@login_required
def home(request):
    return render(request,'home.html')
    

@login_required
def todo_add(request):
    if request.method=='POST':
        title=request.POST.get('title')
        discription=request.POST.get('discription')
        date=request.POST.get('date')
        Todo.objects.create(title=title,discription=discription,date=date)
        return redirect('list_todo')
    else:
        return render(request,'home.html')


@login_required
def list_todo(request):
    context ={}
    context["dataset"] = Todo.objects.all()
    return render(request, "list_todo.html", context)

       
# @login_required
# def edit_todo(request,pk):
#     if request.method=='GET':
#         if Todo.objects.filter(pk=pk).exists():
#             print('Exists')
#             return render(request,'edit_todo.html')
#         else:
#             print('not exists')
#             return redirect('update_todo')
#     else:
#         return redirect('update_todo')


def update_todo(request,pk):        
    if request.method=='POST':
        update=Todo.objects.get(id=pk)
        title=request.POST.get('title')
        discription=request.POST.get('discription')
        date=request.POST.get('date')
        update.title=title
        update.discription=discription
        update.date=date
        update.save()
        return redirect('list_todo')
    else:
        data=Todo.objects.get(id=pk)
        return render(request,'update_todo.html',{'data':data})

@login_required
def del_todo(request,pk):
    if request.method=="GET":
        data=Todo.objects.get(id=pk)
        data.delete()
        return redirect('list_todo')
    else:
        return redirect('list_todo')


            
    






