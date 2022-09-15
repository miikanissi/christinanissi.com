"""The main application's URLs."""
from django.urls import path

from . import views
from .feeds import AtomFeed

urlpatterns = [
    path("", views.index, name="index"),
    path("post", views.post_list, name="post_list"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_tag"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("rss", AtomFeed()),
]
