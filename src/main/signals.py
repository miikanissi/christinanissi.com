from django.db.models.signals import post_save
from PIL import Image

from .models import ContentImage


def content_image_compressor(sender, **kwargs):
    if kwargs["created"]:
        with Image.open(kwargs["instance"].image.path) as image:
            image.save(kwargs["instance"].image.path, optimize=True)


post_save.connect(content_image_compressor, sender=ContentImage)
