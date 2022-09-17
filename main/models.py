from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))


class Writing(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writings")
    tags = TaggableManager(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("writing_detail", kwargs={"slug": str(self.slug)})

    def get_description(self):
        return self.content


class Art(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="arts")
    tags = TaggableManager(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("art_detail", kwargs={"slug": str(self.slug)})

    def get_description(self):
        return self.description


class ArtImage(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    art = models.ForeignKey(Art, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title
