# Generated by Django 4.1.1 on 2022-10-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("findyourpalapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profilepic.png", upload_to="profile_pictures"
            ),
        ),
    ]