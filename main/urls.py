"""The main application's URLs."""
from django.urls import path

from . import views
from .feeds import AtomFeed

urlpatterns = [
    path("", views.index, name="index"),
    path("content", views.content_list, name="content_list"),
    path("writing", views.content_list, {"category": 2}, name="writing_list"),
    path(
        "writing/tag/<slug:tag_slug>/",
        views.content_list,
        {"category": 2},
        name="writing_tag",
    ),
    path(
        "writing/<slug:slug>/",
        views.content_detail,
        {"category": 2},
        name="writing_detail",
    ),
    path("art", views.content_list, {"category": 1}, name="art_list"),
    path(
        "art/tag/<slug:tag_slug>/", views.content_list, {"category": 1}, name="art_tag"
    ),
    path("art/<slug:slug>/", views.content_detail, {"category": 1}, name="art_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("rss", AtomFeed()),
    path("favicon-32x32.png", views.favicon_32),
    path("favicon-16x16.png", views.favicon_16),
    path("favicon.ico", views.favicon),
    path("apple-touch-icon.png", views.apple_touch_icon),
    path("site.webmanifest", views.manifest),
    path("safari-pinned-tab.svg", views.mask_icon),
    path("android-chrome-192x192.png", views.android_chrome_192),
    path("android-chrome-512x512.png", views.android_chrome_512),
    path("browserconfig.xml", views.browserconfig),
    path("mstile-150x150.png", views.mstile),
]
