import environ
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from taggit.models import Tag

from .forms import ContactForm
from .models import Content

env = environ.Env(
    EMAIL_FROM=(str, "example@example.com"), EMAIL_TO=(str, "example@example.com")
)


def index(request):
    contents = Content.objects.filter(
        status=1, publish_date__lt=timezone.now()
    ).order_by("-publish_date")[:12]
    return render(request, "index.html", {"contents": contents})


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry - %s" % form.cleaned_data["name"]
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            email = EmailMessage(
                subject,
                message,
                env("EMAIL_FROM"),
                [env("EMAIL_TO")],
                reply_to=[form.cleaned_data["email"]],
            )
            try:
                email.send()
                messages.success(
                    request,
                    "Your message was sent, I will get back to you shortly, thank you!",
                )
                return HttpResponseRedirect(reverse(contact))
            except BadHeaderError:
                messages.error(
                    request,
                    "Something went wrong. Please try again.",
                )
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def content_list(request, category=None, tag_slug=None):
    template_name = "content_list.html"
    tag = None
    if category:
        contents = Content.objects.filter(
            status=1, publish_date__lt=timezone.now(), category=category
        ).order_by("-publish_date")
    else:
        contents = Content.objects.filter(
            status=1, publish_date__lt=timezone.now()
        ).order_by("-publish_date")
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        contents = contents.filter(tags__in=[tag])
    default_page = 1
    contents_per_page = 12
    page_number = request.GET.get("page", default_page)
    paginator = Paginator(contents, contents_per_page)
    try:
        contents_page = paginator.page(page_number)
    except PageNotAnInteger:
        contents_page = paginator.page(default_page)
    except EmptyPage:
        contents_page = paginator.page(paginator.num_pages)
    return render(
        request,
        template_name,
        {
            "contents_page": contents_page,
            "category": category,
            "tag": tag,
        },
    )


def content_detail(request, slug):
    template_name = "content_detail.html"
    content = get_object_or_404(Content, slug=slug)
    return render(request, template_name, {"content": content})
