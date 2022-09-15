from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "tags", "created_on", "updated_on")
    list_filter = ("status", "tags", "created_on")
    search_fields = ["title", "content", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)
