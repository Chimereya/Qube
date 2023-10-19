from django.shortcuts import render, redirect, get_object_or_404
from . import views
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
from django.urls import reverse


def homepage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'core/home.html', context)


# detail
def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'core/detail.html', {'post': post})


def reply_post(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            parent_id = request.POST.get('parent')
            post_url = request.POST.get('post_url')
            reply = form.save(commit=False)
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
            return redirect(post_url,  reply.id)
    return redirect('/')


@login_required(login_url='user:login')
def ask_question(request):
    post = PostForm(request.POST)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('core:home')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'core/ask.html', context)


# update post
@login_required(login_url='user:login')
def update_question(request, pk):
    update = get_object_or_404(Post, id=pk)
    form = PostForm(instance=update)
    if request.user == update.author:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=update)
            if form.is_valid():
                form.save()
                messages.success(request, "item sucessfully updated")
                return redirect('core:home')

    else:
        return redirect('core:home')
    return render(request, 'core/update.html', {'form': form})


# delete post
@login_required(login_url='user:login')
def delete_view(request, pk):
    item = get_object_or_404(Post, id=pk)
    if request.user == item.author:
        if request.method == 'POST':
            item.delete()
            messages.success(request, "item sucessfully deleted")
            return redirect('core:home')
    else:
        return redirect('core:home')
    return render(request, 'core/delete.html', {'item': item})

@login_required(login_url='user:login')
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if request.user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('core:detail', pk)

    
