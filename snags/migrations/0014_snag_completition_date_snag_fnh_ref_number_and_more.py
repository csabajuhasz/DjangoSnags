# Generated by Django 4.2.5 on 2023-11-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snags", "0013_alter_snag_am_pm"),
    ]

    operations = [
        migrations.AddField(
            model_name="snag",
            name="completition_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="snag",
            name="fnh_ref_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="snag",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
