from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(" ", "_")
    return f"{name}/images/{filename}"


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length__lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(
        ImageAlbum, related_name="images", on_delete=models.CASCADE
    )


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
    album = models.OneToOneField(
        ImageAlbum, related_name="model", on_delete=models.CASCADE
    )
    description = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("art_detail", kwargs={"slug": str(self.slug)})

    def get_description(self):
        return self.description
