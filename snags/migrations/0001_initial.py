# Generated by Django 4.2.4 on 2023-08-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Snag",
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
                ("address", models.CharField(max_length=200)),
                ("post_code", models.CharField(max_length=200)),
                ("plot_number", models.PositiveIntegerField()),
                ("ref_number", models.CharField(max_length=200)),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("phone_number", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=200)),
                ("snag_details", models.CharField(max_length=500)),
                ("notes", models.CharField(max_length=500)),
            ],
        ),
    ]
