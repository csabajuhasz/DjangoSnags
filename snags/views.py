from django.shortcuts import render
from .models import Snag


# Create your views here.


def index(request):
    return render(request, "snags/index.html", {"snags": Snag.objects.all()})
