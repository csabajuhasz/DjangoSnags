from django.contrib import admin
from .models import Operative, Detail, Job

# Register your models here.
admin.site.register(
    Operative,
)
admin.site.register(
    Detail,
)

admin.site.register(
    Job,
)
