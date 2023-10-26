from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['question',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        

        