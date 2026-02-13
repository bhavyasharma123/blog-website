from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Blog, Category, Comment
from .forms import BlogForm

# --- Main Dashboard ---
def home(request):
    """
    Displays the CORE dashboard. Includes logic for category filtering
    and fetches all blogs if no filter is applied.
    """
    category_name = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_name:
        blogs = Blog.objects.filter(category__name=category_name, status='published').order_by('-created_at')
    else:
        # Fetching all published blogs for the grid
        blogs = Blog.objects.filter(status='published').order_by('-created_at')
    
    return render(request, 'main/home.html', {
        'blogs': blogs, 
        'categories': categories, 
        'selected_category': category_name
    })

# --- Wide Workstation Article Creator ---
@login_required(login_url='login')
def create_blog(request):
    """
    Logic for the wide-layout article editor. 
    Handles form submission and slug generation.
    """
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            # Automatically creates URL-friendly slugs (e.g., 'Modern Bridge Design')
            blog.slug = slugify(blog.title)
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    
    return render(request, 'main/create_blog.html', {'form': form})

# --- Immersive Detail & Discussion ---
def blog_detail(request, slug):
    """
    Displays the article text inside the glassmorphism hero background.
    The discussion section is handled separately below the hero area.
    """
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all().order_by('-created_at')
    
    if request.method == "POST":
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            Comment.objects.create(blog=blog, name=name, text=text)
        # Refresh the page to show the new comment
        return redirect('blog_detail', slug=slug)
        
    return render(request, 'main/blog_detail.html', {
        'blog': blog, 
        'comments': comments
    })

# --- System Statistics ---
@login_required(login_url='login')
def more_page(request):
    """
    Provides data for the system monitoring page.
    """
    context = {
        'total_posts': Blog.objects.count(),
        'categories': Category.objects.all(),
        'total_comments': Comment.objects.count(),
        'active_user': request.user
    }
    return render(request, 'main/more.html', context)

# --- Security & Auth ---
def login_page(request):
    """Handles secure user entry."""
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html')

def logout_user(request):
    """Closes the active session."""