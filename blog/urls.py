from django.urls import path
from blog import views
from .views import *


urlpatterns = [
    path("", views.blog, name="blog"),
    path("article/<str:slug>/", views.detail, name="detail"),
    path("create_post/", views.createPost, name="create_post"),
    path("create_category/", views.add_category, name="create_category"),
    path("category/<str:slug>/", views.Category, name="category"),
    path("update_post/<str:slug>/", views.updatePost, name="update_post"),
    path("delete_post/<str:slug>/", views.deletePost, name="delete_post"),
    
    path("user_profile/<str:pk>/", views.Profile, name="profile"),
    path("my_account/", views.account, name="account"),
    path("update_profile/", views.UpdateProfile, name="update_profile"),
    path("delete_profile/", views.DeleteProfile, name="delete_profile"),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile'),
    
    path('search/', views.search, name='search'),
]