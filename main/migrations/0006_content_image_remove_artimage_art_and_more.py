# Generated by Django 4.1.1 on 2022-09-25 20:54
import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0005_writing_teaser_alter_art_slug_alter_art_title_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("title", models.CharField(max_length=128, unique=True)),
                ("slug", models.SlugField(max_length=128, unique=True)),
                ("category", models.IntegerField(choices=[(1, "Art"), (2, "Writing")])),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("teaser", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="writings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("caption", models.TextField(blank=True)),
                ("image", models.ImageField(upload_to="content/")),
                (
                    "content",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="main.content",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="artimage",
            name="art",
        ),
        migrations.RemoveField(
            model_name="writing",
            name="author",
        ),
        migrations.RemoveField(
            model_name="writing",
            name="tags",
        ),
        migrations.DeleteModel(
            name="Art",
        ),
        migrations.DeleteModel(
            name="ArtImage",
        ),
        migrations.DeleteModel(
            name="Writing",
        ),
    ]
