# Generated by Django 4.2.4 on 2023-09-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("operatives", "0008_detail_post_code_alter_detail_wage"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="post_code",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]