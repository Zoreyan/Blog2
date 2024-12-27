from django.shortcuts import render, redirect
from app.models import Post
from .forms import PostForm, SignUpForm

from django.contrib.auth import login, logout, authenticate


def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):

    posts = Post.objects.all()

    search_q = request.GET.get('search')
    
    if search_q:
        posts = Post.objects.filter(title__contains=search_q)


    context = {
        'posts': posts,
        'search_q': search_q
    }
    return render(request, 'app/index.html', context)

def about_us(request):
    return render(request, 'app/about_us.html', )

def contacts(request):
    return render(request, 'app/contacts.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'app/login.html')

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'app/sign_up.html', context)

def profile(request):
    return render(request, 'app/profile.html')

def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post
    }
    return render(request, 'app/post_details.html', context)


def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'app/new_post.html', context)

def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'app/update_post.html', context)


def my_posts(request):
    return render(request, 'app/my_posts.html')

def post_delete(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    return render(request, 'app/post_delete.html')