from django.urls import path
from .views import (
    HomeListView,
    TodoCreateView,
    TodoDeleteView,
    TodoUpdateView,
    )

urlpatterns = [
    # path('login',login_form,name='login_form'),
    # path('signup',signup,name='signup'),
    # path('logout',logout_form,name='logout'),
    path('del_todo/<int:pk>',TodoDeleteView.as_view(),name='del_todo'),
    path('update_todo/<int:pk>',TodoUpdateView.as_view(),name='update_todo'),
    path('todo_add/',TodoCreateView.as_view(),name='todo_add'),
    path('',HomeListView.as_view(),name='home'),
]