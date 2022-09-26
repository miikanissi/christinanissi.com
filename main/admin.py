from django.contrib import admin
from django_summernote.admin import SummernoteInlineModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import Content
from .models import Image


class ImageAdminInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Image


@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin):
    inlines = [ImageAdminInline]
    list_display = (
        "title",
        "slug",
        "category",
        "tag_list",
        "created_on",
        "updated_on",
        "status",
    )
    list_filter = ("category", "tags", "created_on", "status")
    search_fields = ["title", "description", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    class Meta:
        model = Content


@admin.register(Image)
class ImageAdmin(SummernoteModelAdmin):
    list_display = ("title", "caption", "image")
    search_fields = ["title", "caption"]
