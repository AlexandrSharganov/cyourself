from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.core.cache import cache
from django.core.mail import send_mail

from core.otp_generator import generate_otp_code
from users.models import User
from users.tasks import send_otp_to_user_email

from .forms import UserCreationForm, LoginForm, PassResetForm, OTPForm


def register_user(request):
    template = 'users/registration.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            key = request.session.session_key
            otp_code = generate_otp_code()
            value = {
                'email': form.cleaned_data.get('email'),
                'password': form.cleaned_data.get('password1'),
                'otp_code': otp_code
            }
            cache.set(
                key=key,
                value=value
            )
            send_otp_to_user_email.delay(
                recipient_list=[form.cleaned_data.get('email')],
                message=f'OTP code: {otp_code}'
            )
            return redirect('users:confirm_signup_by_otp')
        return render(request, template, {'form': form})
    form = UserCreationForm()
    return render(request, template, {'form': form})

def confirm_signup_by_otp(request):
    template = 'users/otp_confirm.html'
    if request.method == 'POST':
        form = OTPForm(request.POST, request=request)
        if form.is_valid():
            email = cache.get(request.session.session_key)['email']
            password = cache.get(request.session.session_key)['password']
            user, created = User.objects.get_or_create(
                email=email
            )
            if created:
                user.set_password(password)
                user.save()
            return redirect('users:login')
        return render(request, template, {'form': form})
    form = OTPForm()
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
                return redirect('/')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, template_name, {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('/')
