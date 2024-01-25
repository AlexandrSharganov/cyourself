from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

from .forms import UserCreationForm, LoginForm, PassResetForm


def register_user(request):
    template = 'users/registration.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        return render(request, template, {'form': form})
    form = UserCreationForm()
    return render(request, template, {'form': form})


    
def login_user(request):
    template_name = 'users/login.html'

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard:dash')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, template_name, {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('dashboard:dash')

# def password_reset(request):
#     template = 'users/password_reset.html'
#     if request.method == 'POST':
#         form = PassResetForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             return redirect('users:link_sended')
#         return render(request, template, {'form': form})
#     form = PassResetForm()
#     return render(request, template, {'form': form})

# def link_sended(request):
#     template = 'users/link_sended.html'
#     return render(request, template)