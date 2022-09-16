from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from taggit.models import Tag

from .models import Art
from .models import Writing


def index(request):
    return render(request, "index.html")


def writing_detail(request, slug):
    template_name = "writing_detail.html"
    writing = get_object_or_404(Writing, slug=slug)
    return render(request, template_name, {"writing": writing})


def writing_list(request, tag_slug=None):
    template_name = "writing_list.html"
    tag = None
    writings = Writing.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(writings, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        writings = writings.filter(tags__in=[tag])
    return render(
        request, template_name, {"writings": writings, "page_obj": page_obj, "tag": tag}
    )


def art_detail(request, slug):
    template_name = "art_detail.html"
    art = get_object_or_404(Art, slug=slug)
    return render(request, template_name, {"art": art})


def art_list(request, tag_slug=None):
    template_name = "art_list.html"
    tag = None
    arts = Art.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(arts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        arts = arts.filter(tags__in=[tag])
    return render(
        request, template_name, {"arts": arts, "page_obj": page_obj, "tag": tag}
    )
