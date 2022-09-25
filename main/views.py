from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from taggit.models import Tag

from .models import Content


def index(request):
    contents = Content.objects.filter(status=1).order_by("-created_on")[:12]
    return render(request, "index.html", {"contents": contents})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def content_list(request, category=None, tag_slug=None):
    template_name = "content_list.html"
    tag = None
    if category:
        contents = Content.objects.filter(status=1, category=category).order_by(
            "-created_on"
        )
    else:
        contents = Content.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(contents, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        contents = contents.filter(tags__in=[tag])
    return render(
        request,
        template_name,
        {"contents": contents, "category": category, "page_obj": page_obj, "tag": tag},
    )


def content_detail(request, slug, category=None):
    template_name = "content_detail.html"
    content = get_object_or_404(Content, slug=slug)
    return render(request, template_name, {"content": content, "category": category})
