# Generated by Django 4.1.1 on 2022-12-21 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_remove_story_created_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="story",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
