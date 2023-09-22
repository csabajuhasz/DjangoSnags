# Generated by Django 4.2.4 on 2023-09-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snags", "0009_snag_site"),
    ]

    operations = [
        migrations.AddField(
            model_name="snag",
            name="am_pm",
            field=models.CharField(
                choices=[("AM", "AM"), ("PM", "PM")], default="AM", max_length=2
            ),
        ),
        migrations.AlterField(
            model_name="snag",
            name="site",
            field=models.CharField(max_length=200),
        ),
    ]
