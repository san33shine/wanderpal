# Generated by Django 4.1.1 on 2022-10-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_contactus"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactus",
            name="contact_subject",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]