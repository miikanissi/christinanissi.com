# Generated by Django 4.1.1 on 2022-10-04 21:43
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_rename_image_contentimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contentimage",
            name="title",
            field=models.CharField(
                blank=True,
                help_text="Defaults to filename if left blank.",
                max_length=255,
                null=True,
            ),
        ),
    ]