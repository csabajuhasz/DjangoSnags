from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Snag(models.Model):
    status_open = "Open"
    status_closed = "Closed"
    status_delivery = "Parts required"

    status_choices = [
        (status_open, "Open"),
        (status_closed, "Closed"),
        (status_delivery, "Parts required"),
    ]

    am_pm_am = "AM"
    am_pm_pm = "PM"
    am_pm_pm = "Any time"

    am_pm_choices = [
        (am_pm_am, "AM"),
        (am_pm_pm, "PM"),
        (am_pm_pm, "Any time"),
    ]

    site = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    plot_number = models.PositiveIntegerField()
    ref_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    snag_details = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    booked_date = models.DateField(null=True)
    am_pm = models.CharField(max_length=10, choices=am_pm_choices, default=am_pm_am)
    status = models.CharField(
        max_length=20, choices=status_choices, default=status_open
    )
    created_at = models.DateTimeField(auto_now_add=True)
    fnh_ref_number = models.CharField(max_length=200, blank=True)
    completition_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.address

    # def get_absolute_url(self):
    # return reverse("admin_snag_pdf", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["booked_date"]
