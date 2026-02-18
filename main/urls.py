from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<slug:slug>/', views.edit_blog, name='edit_blog'), # Added Edit URL
    path('create/', views.create_blog, name='create_blog'),
    path('blog-info/', views.blog_info, name='blog_info'),
    path('about/', views.about_page, name='about'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]