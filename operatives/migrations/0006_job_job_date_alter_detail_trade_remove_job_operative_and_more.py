# Generated by Django 4.2.4 on 2023-09-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("operatives", "0005_date_operative"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="job_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="detail",
            name="trade",
            field=models.CharField(max_length=200),
        ),
        migrations.RemoveField(
            model_name="job",
            name="operative",
        ),
        migrations.AlterField(
            model_name="operative",
            name="operative_created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name="Date",
        ),
        migrations.AddField(
            model_name="job",
            name="operative",
            field=models.ManyToManyField(to="operatives.operative"),
        ),
    ]