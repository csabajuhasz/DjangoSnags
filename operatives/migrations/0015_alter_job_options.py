# Generated by Django 4.2.5 on 2023-11-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("operatives", "0014_operative_rating"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="job",
            options={"ordering": ["-job_date"]},
        ),
    ]