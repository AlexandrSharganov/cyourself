from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from personal.models import Storage

from .forms import PostForm, CommentForm
from .models import Post, Tag, TagPost, Comment, Like, PostStorage


@login_required
def post_create(request):
    template = 'posts/post_create.html'
    if request.method == 'POST':
        form = PostForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            tags = form.cleaned_data.get('tags').split()
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            result_tags = []
            for tag in tags:
                object, created = Tag.objects.get_or_create(title=tag)
                result_tags.append(
                    TagPost(
                        post=post,
                        tag=object
                    )
                )
            TagPost.objects.bulk_create(result_tags)
            return redirect('personal:personal', request.user.id)
            
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def post_edit(request, pk):
    template = 'posts/post_create.html'
    post = get_object_or_404(Post, id=pk)
    form = PostForm(
        data=request.POST or None,
        instance=post,
        initial={
            'tags': ' '.join([i.tag.title for i in post.tagpost_set.all()])
        }
    )
    if request.user != post.author:
        return redirect('personal:personal', request.user.id)
    if request.method == 'POST':
        if form.is_valid():
            tags = form.cleaned_data.get('tags').split()
            print(tags)
            post.save()
            result_tags = []
            TagPost.objects.filter(post=post).delete()
            for tag in tags:
                tag, tag_created = Tag.objects.get_or_create(name=tag)
                result_tags.append(
                    TagPost(
                        post=post,
                        tag=tag
                    )
                )
            TagPost.objects.bulk_create(result_tags)
            return redirect('personal:personal', request.user.id)  
    context = {
        'form': form,
        'post_id': pk,
        'is_edit': True
    }
    return render(request, template, context)

@login_required
def post_delete(request, pk):
    user = request.user
    post = get_object_or_404(Post, id=pk)
    if user == post.author:
        post.delete()
        return redirect('personal:personal', user.id)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.order_by('-pub_date').filter(post=pk)
    likes = Like.objects.filter(post=pk).count()
    template = 'posts/post_detail.html'
    form = CommentForm()
    context = {
        'likes':likes,
        'post': post,
        'form': form,
        'comments': comments,
        'post_detail': True
    }
    return render(request, template, context)

@login_required
def comments_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid:
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', pk)
        

def news(request):
    posts = Post.objects.all().order_by('-pub_date')
    template = 'posts/storage.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)

@login_required
def storage(request):
    storage = get_object_or_404(Storage, user=request.user)
    posts = Post.objects.filter(poststorage__storage=storage).order_by('poststorage__-add_date')
    print(posts)
    template = 'posts/storage.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)

@login_required
def add_to_storage(request, pk):
    storage = get_object_or_404(Storage, user=request.user)
    post = get_object_or_404(Post, pk=pk)
    # storage = Storage.objects.get(user=request.user)
    # post = Post.objects.get(pk=pk)
    PostStorage.objects.create(storage=storage, post=post)
    return redirect('posts:storage')

@login_required
def delete_from_storage(request, pk):
    storage = get_object_or_404(Storage, user=request.user)
    post = get_object_or_404(Post, pk=pk)
    PostStorage.objects.get(storage=storage, post=post).delete()
    return redirect('posts:storage')

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        Like.objects.create(user=request.user, post=post)
        return redirect('posts:post_detail', pk)
    except:
        return redirect('posts:post_detail', pk)
