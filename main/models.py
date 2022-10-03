from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((1, "Art"), (2, "Writing"))


class Content(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    category = models.IntegerField(choices=CATEGORY)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writings")
    tags = TaggableManager(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    teaser = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": str(self.slug)})

    def get_description(self):
        return self.description


class Image(models.Model):
    title = models.CharField(max_length=128)
    content = models.ForeignKey(
        Content, default=None, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="content/")

    def __str__(self):
        return self.title
