from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache

from users.models import User


class UserCreationForm(forms.Form):
    """A form for creating new users."""
    
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ('email',)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        validate_password(password1)
        if password1 != password2:
            raise forms.ValidationError("Passwords aren't match")
        return password1

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user


class OTPForm(forms.Form):
    
    
    
    opt_field = forms.CharField(
        label='One Time Password',
        help_text='6-digits code have been sended to your email. Please enter it.'
    )
    
    def __init__(self, *args, **kwargs):
        # Передача объекта запроса в качестве аргумента
        self.request = kwargs.pop('request', None)
        super(OTPForm, self).__init__(*args, **kwargs)
    
    def clean_opt_field(self):
        # Check that the two otp_code match
        opt_field = self.cleaned_data.get('opt_field')
        if self.request:
            session_key = self.request.session.session_key
            cache_otp = cache.get(session_key)
            print(cache_otp)
        if opt_field != cache_otp['otp_code']:
            raise forms.ValidationError("Code isn't correct.")
        return opt_field


class LoginForm(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class PassResetForm(forms.Form):
    
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists:
            return forms.ValidationError("User with this email doesn't exist.")
        return email