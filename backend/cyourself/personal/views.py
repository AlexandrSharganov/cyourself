from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from users.models import User
from posts.models import Post
from personal.models import Follow

from .forms import ProfileEditForm
from .models import Profile


def personal_page(request, pk):
    template = 'personal/personal.html'
    person = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=person).prefetch_related('author', 'tagpost_set__tag').order_by('-pub_date')
    context = {}
    if request.user.is_authenticated:
        list_posts_in_storage = Post.objects.filter(poststorage__storage=request.user.storage)
        follows = Follow.objects.filter(follower=request.user.profile, following=person.profile).exists()
        context.update(
            {
                'follows': follows,
                'user': request.user
            }
        )
    else:
        list_posts_in_storage = None
    context.update(
        {
            'person': person,
            'posts': posts,
            'list_posts_in_storage': list_posts_in_storage,
        }
    )
    return render(request, template, context)

def edit_profile(request, pk):
    template = 'personal/personal_edit.html'
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = ProfileEditForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            description = form.cleaned_data.get('description')
            photo = form.cleaned_data.get('photo')
            user.first_name = first_name
            user.last_name = last_name
            user.photo = photo
            user.save()
            profile = get_object_or_404(Profile, author=user)
            profile.description = description
            profile.save()
            return redirect('personal:personal', pk)
        return render(request, template, {'form': form})
    
    form = ProfileEditForm(
        initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'description': user.profile.description,
    }
    )
    return render(request, template, {'form': form})

@login_required
def create_follow(request, pk):
    author = get_object_or_404(User, pk=pk)
    user = request.user
    if user != author:
        Follow.objects.get_or_create(
            follower=user.profile,
            following=author.profile
        )
    return redirect('personal:personal', pk)
    
@login_required
def delete_follow(request, pk):
    author = get_object_or_404(User, pk=pk)
    user = request.user
    Follow.objects.filter(
        follower=user.profile,
        following=author.profile
    ).delete()
    return redirect('personal:personal', pk)

@login_required
def list_follow(request):
    template = 'personal/follow.html'
    followings = User.objects.filter(profile__following__follower=request.user.profile)
    context = {
        'followings': followings,
    }
    return render(request, template, context)
