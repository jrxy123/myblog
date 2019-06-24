from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    post_list = Post.objects.all().order_by('-updated_at')
    pages = Paginator(post_list, 6)
    page = request.GET.get('page')
    posts = pages.get_page(page)
    return render(request, 'blog/index.html', {'posts': posts})#템플릿 변수명: view변수명

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def detail(request, post_id):
    # if request.method == 'POST':
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/detail.html', {'post': post})

def newcomment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('detail', post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/newcomment.html', {'form': form})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/newpost.html', {'form': form})
