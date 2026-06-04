from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('todo/', views.todo, name='todo'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>/', views.delete_todo, name='delete_todo'),
    path('logout/', views.logout, name='logout'),
]