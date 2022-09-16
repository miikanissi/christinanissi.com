from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Art
from .models import Writing


class WritingAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "tags", "created_on", "updated_on")
    list_filter = ("status", "tags", "created_on")
    search_fields = ["title", "content", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


class ArtAdmin(SummernoteModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "tags",
        "created_on",
        "updated_on",
        "album",
    )
    list_filter = ("status", "tags", "created_on")
    search_fields = ["title", "description", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)


admin.site.register(Writing, WritingAdmin)
admin.site.register(Art, ArtAdmin)
