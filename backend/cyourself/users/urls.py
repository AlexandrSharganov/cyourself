from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import (
   PasswordChangeDoneView,
   PasswordResetView,
   PasswordResetDoneView,
   PasswordResetCompleteView,
   PasswordResetConfirmView,
)

from .views import register_user, custom_logout, login_user, confirm_signup_by_otp


app_name = 'users'

urlpatterns = [
    path('registration/', register_user, name='registration'),
    path('confirm_signup_by_otp/', confirm_signup_by_otp, name='confirm_signup_by_otp'),
    path('login/', login_user, name='login'),
    path('logout/', custom_logout, name='logout'),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset.html',
            email_template_name='users/email_reset_pass.html',
            success_url=reverse_lazy("users:link_sended")
        ), 
        name='password_reset'
    ),
    path(
        'password_reset/link_sended/',
        PasswordResetDoneView.as_view(
            template_name='users/link_sended.html'
        ),
        name='link_sended'
    ),
    path(
        'password_reset/new_pass_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url = reverse_lazy("users:pass_done")
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset/pass_done/',
        PasswordResetCompleteView.as_view(
            template_name='users/pass_done.html'
        ),
        name='pass_done'
    ),
]
