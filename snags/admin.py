from django.contrib import admin
from . import models


@admin.register(models.Snag)
class SnagAdmin(admin.ModelAdmin):
    actions = ["close_status"]
    list_display = ["address", "site", "status", "booked_date", "am_pm"]
    list_editable = ["status", "booked_date", "am_pm"]
    list_per_page = 10
    search_fields = ["address__icontains", "booked_date"]
    list_filter = ["site", "booked_date", "status", "am_pm"]

    @admin.action(description="Close Snags")
    def close_status(self, request, queryset):
        updated_status = queryset.update(status="Closed")
        self.message_user(request, f"{updated_status} were successfully Closed")


# Register your models here.
# admin.site.register(Snag, SnagAdmin)
