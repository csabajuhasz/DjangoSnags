from django.contrib import admin
from . import models


@admin.register(models.Snag)
class SnagAdmin(admin.ModelAdmin):
    list_display = ["address", "status", "booked_date", "am_pm"]
    list_editable = ["status", "booked_date", "am_pm"]
    list_per_page = 10
    search_fields = ["address__icontains", "booked_date"]
    list_filter = ["site", "booked_date", "status", "am_pm"]


# Register your models here.
# admin.site.register(Snag, SnagAdmin)
