from django.db import models
from django.utils import timezone


class Operative(models.Model):
    one = "Poor"
    two = "Room for Improvement"
    tree = "Good"
    four = "Dog's bollocks"

    rating_choices = [
        (one, "Poor"),
        (two, "Room for Improvement"),
        (tree, "Good"),
        (four, "Dog's bollocks"),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    operative_created_at = models.DateField(auto_now_add=True)
    rating = models.CharField(max_length=4, choices=rating_choices, default=tree)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name"]


class Detail(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    post_code = models.CharField(blank=True, max_length=200, null=True)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    trade = models.CharField(max_length=200)
    card = models.CharField(max_length=200)
    driving_license = models.CharField(max_length=200)
    wage = models.PositiveIntegerField()
    operative = models.OneToOneField(
        Operative, on_delete=models.CASCADE, primary_key=True
    )

    def __str__(self):
        return f"Trade:  {self.trade}"


class Job(models.Model):
    operatives = models.ManyToManyField(Operative)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    post_code = models.CharField(blank=True, max_length=200, null=True)
    job_created_at = models.DateTimeField(auto_now_add=True)
    job_date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.location

    class Meta:
        ordering = ["-job_date"]


# Create your models here.
