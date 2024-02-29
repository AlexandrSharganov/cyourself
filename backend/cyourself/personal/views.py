from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404

from users.models import User
from posts.models import Post

from .forms import ProfileEditForm
from .models import Profile


def personal_page(request, pk):
    template = 'personal/personal.html'
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user).order_by('-pub_date')
    context = {
        'user': user,
        'posts': posts
    }
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
