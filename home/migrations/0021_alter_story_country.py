# Generated by Django 4.1.1 on 2022-12-25 05:50

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_story_country_alter_story_story_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="country",
            field=django_countries.fields.CountryField(max_length=746, multiple=True),
        ),
    ]
