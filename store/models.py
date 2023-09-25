from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=200)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Site(models.Model):
    title = models.CharField(max_length=200)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Material(models.Model):
    title = models.CharField(max_length=200)
    inventory = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
