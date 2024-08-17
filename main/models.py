from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = CKEditor5Field('Text', config_name='extends')
    video = models.FileField(upload_to='video/project_videos', null=True, blank=True)
    image = models.ImageField(upload_to='images/project_images')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    message =  models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

