from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied
from .models import Blog, Category, Comment
from .forms import BlogForm

def home(request):
    category_name = request.GET.get('category')
    categories = Category.objects.all()
    blogs = Blog.objects.filter(status='published').order_by('-created_at')
    if category_name:
        blogs = blogs.filter(category__name=category_name)
    return render(request, 'main/home.html', {'blogs': blogs, 'categories': categories})

def blog_info(request):
    return render(request, 'main/blog_info.html', {
        'total_posts': Blog.objects.count(),
        'categories': Category.objects.all(),
        'total_comments': Comment.objects.count(),
    })

def about_page(request):
    return render(request, 'main/about.html', {
        'about_title': "The CORE Mission",
        'about_text': "CORE is a dedicated platform for documenting modern infrastructure."
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            Comment.objects.create(blog=blog, name=name, text=text)
        return redirect('blog_detail', slug=slug)
    return render(request, 'main/blog_detail.html', {'blog': blog, 'comments': blog.comments.all()})

@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.slug = slugify(blog.title)
            blog.save()
            return redirect('home')
    return render(request, 'main/create_blog.html', {'form': BlogForm()})

# --- NEW: PROTECTED EDIT VIEW ---
@login_required(login_url='login')
def edit_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    # Permission Check: Only the author can edit
    if blog.author != request.user:
        raise PermissionDenied
        
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'main/create_blog.html', {'form': form, 'edit_mode': True})

def login_page(request):
    if request.method == 'POST':
        u, p = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')