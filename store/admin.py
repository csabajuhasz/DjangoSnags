from django.contrib import admin
from . import models


class MaterialInline(admin.StackedInline):
    model = models.Material


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "update"]
    list_per_page = 10
    inlines = [MaterialInline]


@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ["title", "update"]
    list_per_page = 10


@admin.register(models.Material)
class Materialdmin(admin.ModelAdmin):
    list_display = ["title", "inventory", "update", "collection", "site"]
    list_per_page = 10
    list_filter = ["site", "collection"]
    list_editable = ["inventory"]
    search_fields = ["title"]
