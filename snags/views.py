from django.shortcuts import render, redirect
from .models import Snag
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddSnagForm

# Create your views here.


def core(request):
    return render(request, "core.html", {})


def index(request):
    snags = Snag.objects.all().order_by("-status", "site", "booked_date")

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
        return render(request, "snags/home.html", {"snags": snags})


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
        customer_snag = Snag.objects.get(id=pk)
        return render(request, "snags/customer.html", {"customer_snag": customer_snag})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("snags/home")


def delete_snag(request, pk):
    if request.user.is_authenticated:
        delete_it = Snag.objects.get(id=pk)
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
        )
        snags = Snag.objects.filter(multiple)
        return render(
            request,
            "search.html",
            {"searched": searched, "snags": snags},
        )
    else:
        return render(request, "search.html", {})
