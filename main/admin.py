from django.contrib import admin
from django_summernote.admin import SummernoteInlineModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import Art
from .models import ArtImage
from .models import Writing


class ArtImageAdminInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = ArtImage


@admin.register(Art)
class ArtAdmin(SummernoteModelAdmin):
    inlines = [ArtImageAdminInline]
    list_display = (
        "title",
        "slug",
        "status",
        "tag_list",
        "created_on",
        "updated_on",
    )
    list_filter = ("status", "tags", "created_on")
    search_fields = ["title", "description", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    class Meta:
        model = Art


@admin.register(ArtImage)
class ArtImageAdmin(SummernoteModelAdmin):
    list_display = ("title", "caption", "image")
    search_fields = ["title", "caption"]


@admin.register(Writing)
class WritingAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "tag_list", "created_on", "updated_on")
    list_filter = ("status", "tags", "created_on")
    search_fields = ["title", "content", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    class Meta:
        model = Writing
