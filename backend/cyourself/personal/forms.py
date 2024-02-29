from django import forms


class ProfileEditForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        help_text='Tell about yourself.'
    )
    photo = forms.ImageField(
        required=False,
    )
    