# Generated by Django 4.2.5 on 2023-09-25 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Store",
            new_name="Material",
        ),
    ]