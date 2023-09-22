from django.db import models
from django.utils import timezone


class Operative(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    operative_created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Detail(models.Model):
    address = models.CharField(max_length=200)
    post_code = models.CharField(blank=True, max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
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
    post_code = models.CharField(blank=True, max_length=200)
    job_created_at = models.DateTimeField(auto_now_add=True)
    job_date = models.DateField(null=True)

    def __str__(self):
        return f" {self.description} at  {self.location} "


# Create your models here.
