from django import forms
from django.forms.models import inlineformset_factory

from .models import Tag, Post, TagPost, Comment


class TagPostForm(forms.ModelForm):
    
    class Meta:
        model = TagPost
        fields = '__all__'


class PostForm(forms.ModelForm):
    
    tags = forms.CharField(
        required=True,
        help_text='''Please, write some keywords\
                     in this area using space between\
                     to describe your article.'''
    )
    
    class Meta:
        model = Post
        fields = ('title', 'text', )


class CommentForm(forms.ModelForm):
    
    text = forms.CharField(widget=forms.Textarea(attrs={'style': 'max-height:100px;'}))
    
    class Meta:
        model = Comment
        fields =  ('text',)