from django.contrib import admin
from django.urls import path 
from . import views


urlpatterns = [
    # API to coments post here
    path("postComment" ,views.postComment , name="postComment"),
    path("", views.blogHome , name="blogHome"),
    path("<str:slug>", views.blogPost, name="blogPost"),
]