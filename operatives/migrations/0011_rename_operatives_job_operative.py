# Generated by Django 4.2.5 on 2023-09-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("operatives", "0010_alter_job_options_alter_operative_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="operatives",
            new_name="operative",
        ),
    ]