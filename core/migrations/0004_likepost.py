# Generated by Django 4.2.4 on 2023-09-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_post_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
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
                ("post_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
    ]
