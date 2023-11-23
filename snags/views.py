from django.shortcuts import render, redirect, get_object_or_404
from .models import Snag
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddSnagForm
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator

# Create your views here.


def core(request):
    return render(request, "core.html", {})


def snag_list(request):
    p = Paginator(
        Snag.objects.all().order_by(
            "-status",
            "booked_date",
            "am_pm",
            "site",
        ),
        5,
    )

    page_number = request.GET.get("page")
    snags = p.get_page(page_number)
    return render(request, "snags/snag_list.html", {"snags": snags})


def home(request):
    # Check to see if logged in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Nice to see you again Sunshine  :)")
            return redirect("core")
        else:
            messages.success(request, "Error ,please try again")
            return redirect("snags/home")
    else:
        return redirect("snags/snag_list")


def logout_user(request):
    logout(request)
    messages.success(request, "See you later .... aligator :)")
    return redirect("snags/home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect("snags/home")
    else:
        form = SignUpForm()
        return render(request, "snags/register.html", {"form": form})
        messages.succes(request, "Holly Guacamolyy something is not mstchinh")
    return render(request, "snags/register.html", {"form": form})


def customer_snag(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        # customer_snag = Snag.objects.get(id=pk)
        customer_snag = get_object_or_404(
            Snag,
            id=pk,
        )
        return render(request, "snags/customer.html", {"customer_snag": customer_snag})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("snags/home")


def delete_snag(request, pk):
    if request.user.is_authenticated:
        # delete_it = Snag.objects.get(id=pk)
        delete_it = get_object_or_404(
            Snag,
            id=pk,
        )

        delete_it.delete()
        messages.success(request, "You have deleted  succesfully")
        return redirect("snags/home")

    else:
        messages.success(request, "You have to log in ")
        return redirect("snags/home")


def add_snag(request):
    form = AddSnagForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_snag = form.save()
                messages.success(request, "Snag Added...")
                return redirect("snags/home")
        return render(request, "snags/add_snag.html", {"form": form})

    elif request.method == "POST":
        if form.is_valid():
            add_snag = form.save()
            messages.success(request, "Snag Added...")
            return redirect("snags/home")
        return render(request, "snags/add_snag.html", {"form": form})

    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("snags/home")


def update_snag(request, pk):
    if request.user.is_authenticated:
        current_snag = Snag.objects.get(id=pk)
        form = AddSnagForm(request.POST or None, instance=current_snag)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Changes has been Updated...")
            return redirect("snags/home")
        return render(request, "snags/update_snag.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("snags/home")


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        # snags = Snag.objects.filter(address__icontains=searched)
        multiple = Q(
            Q(address__icontains=searched)
            | Q(status__icontains=searched)
            | Q(site__icontains=searched)
            | Q(booked_date__icontains=searched)
        )
        snags = Snag.objects.filter(multiple)

        return render(
            request,
            "search.html",
            {"searched": searched, "snags": snags},
        )

    else:
        return render(request, "search.html", {})


def snag_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=snags.csv"

    # Create csv writer
    writer = csv.writer(response)

    # Designate the model
    snags = Snag.objects.all()

    # Add Columns:
    writer.writerow(
        [
            "Site",
            "Address",
            "Post Code",
            "Plot Nr.",
            "Ref. Nr.",
            "First Name",
            "Last Name",
            "Phone Nr.",
            "E mail",
            "Details",
            "Notes",
            "Date",
            "AM / PM",
            "Status",
            "Created at",
        ]
    )

    # Loop through:
    for snag in snags:
        writer.writerow(
            [
                snag.site,
                snag.address,
                snag.post_code,
                snag.plot_number,
                snag.ref_number,
                snag.first_name,
                snag.last_name,
                snag.phone_number,
                snag.email,
                snag.snag_details,
                snag.notes,
                snag.booked_date,
                snag.am_pm,
                snag.status,
                snag.created_at,
            ]
        )

    return response


def search_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=searched_snag.csv"

    if request.method == "POST":
        searched = request.POST["searched"]
        # snags = Snag.objects.filter(address__icontains=searched)
        multiple = Q(
            Q(address__icontains=searched)
            | Q(status__icontains=searched)
            | Q(site__icontains=searched)
            | Q(booked_date__icontains=searched)
        )

        # Create csv writer
        writer = csv.writer(response)

        # Designate the model
        snags = Snag.objects.filter(multiple)

        # Add Columns:
        writer.writerow(
            [
                "Site",
                "Address",
                "Post Code",
                "Plot Nr.",
                "Ref. Nr.",
                "First Name",
                "Last Name",
                "Phone Nr.",
                "E mail",
                "Details",
                "Notes",
                "Date",
                "AM / PM",
                "Status",
                "Created at",
            ]
        )

        # Loop through:
        for snag in snags:
            writer.writerow(
                [
                    snag.site,
                    snag.address,
                    snag.post_code,
                    snag.plot_number,
                    snag.ref_number,
                    snag.first_name,
                    snag.last_name,
                    snag.phone_number,
                    snag.email,
                    snag.snag_details,
                    snag.notes,
                    snag.booked_date,
                    snag.am_pm,
                    snag.status,
                    snag.created_at,
                ]
            )

        return response
