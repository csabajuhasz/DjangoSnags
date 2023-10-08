from django.shortcuts import render, redirect
from django.db.models import F
from operatives.models import *
from django.db.models import Q


# from django.contrib.auth import authenticate, login, logout


# from .forms import SignUpForm

# Create your views here.


def operatives(request):
    operatives = Operative.objects.all()

    # operative = Operative.objects.get(id=pk)
    # if request.user.is_authenticated:
    # Look Up Records

    return render(request, "operatives/home.html", {"operatives": operatives})


def individual(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        operatives = Operative.objects.get(id=pk)
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
        ).order_by("job_date", "location")
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
        )

        return render(
            request,
            "operatives/search_job.html",
            {"searched": searched, "jobs": jobs},
        )
    else:
        return render(request, "search.html", {})
