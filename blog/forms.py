from django import forms
from django.forms import *
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'writer', 'likes']
        
        
class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        
        
class CreateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ['slug']
        #fields = ['title', 'slug']
               

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']