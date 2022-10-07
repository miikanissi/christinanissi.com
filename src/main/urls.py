"""The main application's URLs."""
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .feeds import AtomFeed

urlpatterns = [
    path("", views.index, name="index"),
    path("content", views.content_list, name="content_list"),
    path("content/<slug:slug>/", views.content_detail, name="content_detail"),
    path("tag/<slug:tag_slug>/", views.content_list, name="tag"),
    path("writing", views.content_list, {"category": 2}, name="writing_list"),
    path("art", views.content_list, {"category": 1}, name="art_list"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("rss", AtomFeed()),
    path(
        "favicon-32x32.png",
        RedirectView.as_view(url=staticfiles_storage.url("files/favicon-32x32.png")),
    ),
    path(
        "favicon-16x16.png",
        RedirectView.as_view(url=staticfiles_storage.url("files/favicon-16x16.png")),
    ),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("files/favicon.ico")),
    ),
    path(
        "apple-touch-icon.png",
        RedirectView.as_view(url=staticfiles_storage.url("files/apple-touch-icon.png")),
    ),
    path(
        "site.webmanifest",
        RedirectView.as_view(url=staticfiles_storage.url("files/site.webmanifest")),
    ),
    path(
        "safari-pinned-tab.svg",
        RedirectView.as_view(
            url=staticfiles_storage.url("files/safari-pinned-tab.svg")
        ),
    ),
    path(
        "android-chrome-192x192.png",
        RedirectView.as_view(
            url=staticfiles_storage.url("files/android-chrome-192x192.png")
        ),
    ),
    path(
        "android-chrome-512x512.png",
        RedirectView.as_view(
            url=staticfiles_storage.url("files/android-chrome-512x512.png")
        ),
    ),
    path(
        "browserconfig.xml",
        RedirectView.as_view(url=staticfiles_storage.url("files/browserconfig.xml")),
    ),
    path(
        "mstile-150x150.png",
        RedirectView.as_view(url=staticfiles_storage.url("files/mstile-150x150.png")),
    ),
]
