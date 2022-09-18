"""The main application's URLs."""
from django.urls import path

from . import views
from .feeds import AtomFeed

urlpatterns = [
    path("", views.index, name="index"),
    path("writing", views.writing_list, name="writing_list"),
    path("writing/tag/<slug:tag_slug>/", views.writing_list, name="writing_tag"),
    path("writing/<slug:slug>/", views.writing_detail, name="writing_detail"),
    path("art", views.art_list, name="art_list"),
    path("art/tag/<slug:tag_slug>/", views.art_list, name="art_tag"),
    path("art/<slug:slug>/", views.art_detail, name="art_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("rss", AtomFeed()),
]
