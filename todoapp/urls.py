from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',login_form,name='login_form'),
    path('signup',signup,name='signup'),
    path('login',login_form,name='login_form'),
    path('logout',logout_form,name='logout'),
    path('home',home,name='home'),
    path('todo_add',todo_add,name='todo_add'),
    path('list_todo',list_todo,name='list_todo'),
    path('update_todo/<int:pk>',update_todo,name='update_todo'),
    path('del_todo/<int:pk>',del_todo,name='del_todo'),
    # path('edit_todo/<int:pk>',edit_todo,name='edit_todo'),
]