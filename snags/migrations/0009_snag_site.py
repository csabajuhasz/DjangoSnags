# Generated by Django 4.2.4 on 2023-09-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snags", "0008_alter_snag_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="snag",
            name="site",
            field=models.CharField(default=False, max_length=200),
        ),
    ]
