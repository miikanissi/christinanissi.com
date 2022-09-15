from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from taggit.models import Tag

from .models import Post


def index(request):
    return render(request, "index.html")


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    return render(request, template_name, {"post": post})


def post_list(request, tag_slug=None):
    template_name = "post_list.html"
    tag = None
    posts = Post.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    return render(
        request, template_name, {"posts": posts, "page_obj": page_obj, "tag": tag}
    )
