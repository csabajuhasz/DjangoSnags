from django.contrib import admin
from . import models
import csv
import datetime
from .models import Snag
from django.http import HttpResponse

# from django.urls import reverse
# from django.utils.safestring import mark_safe


# def snag_pdf(obj):
# url = reverse("snags:admin_snag_pdf", args=[obj.id])
# return mark_safe(f'<a href="{url}">PDF</a>')


# snag_pdf.short_description = "Defect Notice"


@admin.register(models.Snag)
class SnagAdmin(admin.ModelAdmin):
    actions = ["close_status", "snag_csv"]
    list_display = ["address", "site", "status", "booked_date", "am_pm"]
    list_editable = ["status", "booked_date", "am_pm"]
    list_per_page = 10
    search_fields = ["address__icontains", "booked_date", "site"]
    list_filter = ["site", "booked_date", "status", "am_pm"]

    @admin.action(description="Close Snags")
    def close_status(self, request, queryset):
        updated_status = queryset.update(status="Closed")
        self.message_user(request, f"{updated_status} were successfully Closed")

    def snag_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        content_disposition = f"attachment; filename=snag.csv"
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

    snag_csv.short_description = "Export to CSV"
