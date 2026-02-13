from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_blog, name='create_blog'),
    path('more/', views.more_page, name='more'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]