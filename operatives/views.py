from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from operatives.models import *
from django.db.models import Q
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator


# from django.contrib.auth import authenticate, login, logout


# from .forms import SignUpForm

# Create your views here.


def operatives(request):
    p = Paginator(Operative.objects.all(), 5)

    page_number = request.GET.get("page")
    operatives = p.get_page(page_number)

    # operative = Operative.objects.get(id=pk)
    # if request.user.is_authenticated:
    # Look Up Records

    return render(request, "operatives/home.html", {"operatives": operatives})


def individual(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        # operatives = Operative.objects.get(id=pk)
        operatives = get_object_or_404(
            Operative,
            id=pk,
        )
        individuals = Detail.objects.get(operative_id=pk)
        return render(
            request,
            "operatives/individual.html",
            {"individuals": individuals, "operatives": operatives},
        )
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("snags/home")


def job(request):
    # operatives = Operative.objects.prefetch_related_related("description").all()
    details = (
        Job.objects.values(
            "location", "description", "job_date", "operatives__first_name"
        ).order_by("-job_date", "location")
        # Job.objects.prefetch_related("operatives")
        # .order_by("job_date", "operatives")
        # .all()
    )

    return render(
        request,
        "operatives/detail.html",
        {"jobs": list(details), "operatives": operatives},
    )


def search_job(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        # snags = Snag.objects.filter(address__icontains=searched)

        jobs = Job.objects.filter(
            Q(operatives__first_name__icontains=searched)
            | Q(operatives__last_name__icontains=searched)
            | Q(description__icontains=searched)
            | Q(location__icontains=searched)
        ).values("location", "description", "job_date", "operatives__first_name")

        return render(
            request,
            "operatives/search_job.html",
            {"searched": searched, "jobs": jobs},
        )
    else:
        return render(request, "search.html", {})


def job_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=job.csv"

    if request.method == "POST":
        searched = request.POST["searched"]
        # snags = Snag.objects.filter(address__icontains=searched)
        multiple = Q(
            Q(operatives__first_name__icontains=searched)
            | Q(operatives__last_name__icontains=searched)
            | Q(description__icontains=searched)
            | Q(location__icontains=searched)
        )

        # Create csv writer
        writer = csv.writer(response)

        # Designate the model
        jobs = Job.objects.filter(multiple)

        # Add Columns:
        writer.writerow(
            [
                "Description",
                "Location",
                "Post Code.",
                "Job Date",
            ]
        )

        # Loop through:
        for job in jobs:
            writer.writerow(
                [
                    job.description,
                    job.location,
                    job.post_code,
                    job.job_date,
                ]
            )

        return response
