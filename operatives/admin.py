from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

# from .models import Operative, Detail, Job
from . import models


# Register your models here.
class DetailInline(admin.StackedInline):
    model = models.Detail


@admin.register(models.Operative)
class OperativeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "operative_created_at"]
    list_per_page = 10
    search_fields = ["first_name__istartswith"]
    inlines = [DetailInline]


@admin.register(models.Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ["operative", "phone_number", "email", "trade"]
    list_per_page = 10
    search_fields = ["trade__istartswith"]
    list_filter = ["trade"]


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["location", "description", "job_date"]
    list_per_page = 10
    search_fields = ["location__istartswith"]
    list_filter = ["location", "job_date"]
