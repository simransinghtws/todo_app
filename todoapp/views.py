from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView


from .models import Todo,User
class HomeListView(ListView):
    model = Todo
    context_object_name = "dataset"
    template_name = "home.html"

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title","description","date"]
    template_name = "create-todo.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "update-todo.html"
    fields = ["title","description","date"]


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "delete-todo.html"
    success_url = reverse_lazy("home")

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        repassw=request.POST.get('password2')
        if User.objects.filter(username=name).exists():
            messages.warning(request, 'User Already Exists')
            return render(request,'login.html')
        else:
            if len(passw) >= 8:
                if passw==repassw:
                    User.objects.create_user(username = name, email = email, password = passw)
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
    