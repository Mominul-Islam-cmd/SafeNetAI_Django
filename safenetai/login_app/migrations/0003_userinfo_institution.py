# Generated by Django 4.1 on 2025-02-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_app", "0002_userinfo_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="institution",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
