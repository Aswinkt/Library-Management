"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .import views


urlpatterns = [
    path('users/view/', views.UserListView.as_view(), name='user-list'),
    path('users/add/', views.UserListAdd.as_view(), name='user-list'),
    path('users/update/<int:pk>/', views.UserListUpdate.as_view(), name='user-detail'),
    path('users/delete/', views.UserListAdd.as_view(), name='user-list'),
    path('books/view/', views.BookListView.as_view(), name='user-list'),
    path('books/add/', views.BookListAdd.as_view(), name='user-list'),
    path('books/update/<int:pk>/', views.BookListUpdate.as_view(), name='user-detail'),
    path('books/delete/', views.BookListDelete.as_view(), name='user-list'),
  
]
