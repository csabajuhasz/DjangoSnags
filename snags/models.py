from django.db import models
from django.utils import timezone


# Create your models here.
class Snag(models.Model):
    status_open = "O"
    status_closed = "C"
    status_delivery = "D"

    status_choices = [
        (status_open, "Open"),
        (status_closed, "Closed"),
        (status_delivery, "Waiting for delivery"),
    ]
    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    plot_number = models.PositiveIntegerField()
    ref_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    snag_details = models.TextField()
    notes = models.TextField()
    booked_date = models.DateField(null=True)
    status = models.CharField(max_length=1, choices=status_choices, default=status_open)

    def __str__(self):
        return f"Snag: {self.address} {self.plot_number}"
