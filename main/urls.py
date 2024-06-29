from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("my_projects/", views.Portfolio, name="portfolio"),
    path("my_projects/<str:slug>/", views.Portfolio_detail, name="portfolio_detail")
]