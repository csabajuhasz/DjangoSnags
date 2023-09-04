from django.contrib import admin
from .models import Snag


class SnagAdmin(admin.ModelAdmin):
    list_display = ["address", "status", "booked_date"]
    list_editable = ["status"]
    search_fields = ["address__istartswith", "booked_date"]


# Register your models here.
admin.site.register(Snag, SnagAdmin)
