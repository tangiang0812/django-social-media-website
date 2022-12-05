# Generated by Django 4.1.3 on 2022-12-05 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_followerscount"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment_id", models.CharField(max_length=500)),
                ("user", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
