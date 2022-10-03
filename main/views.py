import environ
from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import FileResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET
from taggit.models import Tag

from .forms import ContactForm
from .models import Content

env = environ.Env(
    EMAIL_FROM=(str, "example@example.com"), EMAIL_TO=(str, "example@example.com")
)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon_32(request):
    file = (settings.BASE_DIR / "static" / "favicon-32x32.png").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon_16(request):
    file = (settings.BASE_DIR / "static" / "favicon-16x16.png").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def apple_touch_icon(request):
    file = (settings.BASE_DIR / "static" / "apple-touch-icon.png").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def manifest(request):
    file = (settings.BASE_DIR / "static" / "site.webmanifest").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def mask_icon(request):
    file = (settings.BASE_DIR / "static" / "safari-pinned-tab.svg").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def android_chrome_192(request):
    file = (settings.BASE_DIR / "static" / "android-chrome-192x192.png").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def android_chrome_512(request):
    file = (settings.BASE_DIR / "static" / "android-chrome-512x512.png").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request):
    file = (settings.BASE_DIR / "static" / "favicon.ico").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def browserconfig(request):
    file = (settings.BASE_DIR / "static" / "browserconfig.xml").open("rb")
    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def mstile(request):
    file = (settings.BASE_DIR / "static" / "mstile-150x150.png").open("rb")
    return FileResponse(file)


def index(request):
    contents = Content.objects.filter(status=1).order_by("-created_on")[:12]
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
