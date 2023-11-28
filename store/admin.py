from django.contrib import admin
from . import models
import csv
import datetime
from .models import Material
from django.http import HttpResponse


class MaterialInline(admin.StackedInline):
    model = models.Material


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "update"]
    list_per_page = 10
    inlines = [MaterialInline]
    search_fields = ["title__istartswith"]


@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ["title", "update"]
    list_per_page = 10
    search_fields = ["title__istartswith"]


@admin.register(models.Material)
class Materialdmin(admin.ModelAdmin):
    actions = ["material_csv"]
    list_display = ["title", "inventory", "update", "collection", "site"]
    list_per_page = 10
    list_filter = ["site", "collection"]
    list_editable = ["inventory"]
    search_fields = ["title__istartswith"]

    def material_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        content_disposition = f"attachment; filename=material.csv"
        response = HttpResponse(content_type="text/csv")
        response["Contet_Disposition"] = content_disposition
        writer = csv.writer(response)
        fields = [
            field
            for field in opts.get_fields()
            if not field.many_to_many and not field.one_to_many
        ]

        writer.writerow([field.name for field in fields])
        for obj in queryset:
            data_row = []
            for field in fields:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime("%d/%m/%Y")
                data_row.append(value)
            writer.writerow(data_row)
        return response

    material_csv.short_description = "Export to CSV"
