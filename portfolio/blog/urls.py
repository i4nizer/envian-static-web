from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('post/', views.blog_post, name="blog_post"),
]