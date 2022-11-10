from django.db.models.signals import post_save
from PIL import Image

from .models import ContentImage


def content_image_compressor(sender, **kwargs):
    if kwargs["created"]:
        with Image.open(kwargs["instance"].image.path) as image:
            max_width = 1920
            max_height = 1080
            width, height = image.size
            resize_ratio = min(max_width / width, max_height / height)
            if resize_ratio < 1:
                new_width = int(width * resize_ratio)
                new_height = int(height * resize_ratio)
                image = image.resize((new_width, new_height))
            # image.save(kwargs["instance"].image.path, quality=80, optimize=True)
            image.save(kwargs["instance"].image.path)


post_save.connect(content_image_compressor, sender=ContentImage)
