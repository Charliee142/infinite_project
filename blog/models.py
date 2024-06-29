from django.db import models
import uuid
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null= True)
    last_name = models.CharField(max_length=50, null= True)
    email = models.EmailField()
    username = models.CharField(max_length=50, null= True)
    profession = models.CharField(max_length=250, null= True)
    image = models.ImageField(blank=True, null=True, upload_to='images/profile_images')
    about = models.TextField()
    website_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    whatsapp_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    upwork_url = models.CharField(max_length=200, null=True, blank=True)
    telegram_url = models.CharField(max_length=200, null=True, blank=True)
    youtube_url = models.CharField(max_length=200, null=True, blank=True)
    github_url = models.CharField(max_length=200, null=True, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    profile_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return f'{self.user.username} Profile' 
    
    def get_absolute_url(self):
        return reverse("index")
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("index")


class Post(models.Model):
    writer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = CKEditor5Field('Text', config_name='extends')
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    image = models.ImageField(upload_to="images/post_images")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    view_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date_commented = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} commented on '{self.post}'"