# Generated by Django 4.1.1 on 2022-09-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="travel_destination",
            new_name="travel_itinerary",
        ),
    ]
