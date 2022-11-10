from django.contrib import admin
from django_summernote.admin import SummernoteInlineModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import Content
from .models import ContentImage


class ImageAdminInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = ContentImage


@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin):
    inlines = [ImageAdminInline]
    list_display = (
        "title",
        "slug",
        "category",
        "tag_list",
        "publish_date",
        "create_date",
        "update_date",
        "status",
    )
    list_editable = ("category", "status")
    list_filter = (
        "category",
        "tags",
        "publish_date",
        "create_date",
        "update_date",
        "status",
    )
    search_fields = ["title", "description", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    class Meta:
        model = Content


@admin.register(ContentImage)
class ImageAdmin(SummernoteModelAdmin):
    list_display = ("title", "image", "image_size")
    search_fields = ["title"]
