from django.shortcuts import render, redirect
from .models import Snag
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.


def index(request):
    snags = Snag.objects.all()

    # Check to see if logged in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome to LCS Snags")
            return redirect("home")
        else:
            messages.success(request, "Error ,please try again")
            return redirect("home")
    else:
        return render(request, "home.html", {"snags": snags})


def logout_user(request):
    logout(request)
    messages.success(request, "You Logged Out succesfully")
    return redirect("home")


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
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})
        messages.succes(request, "Holly Guacamolyy something is not mstchinh")
    return render(request, "register.html", {"form": form})


def customer_snag(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_snag = Snag.objects.get(id=pk)
        return render(request, "customer.html", {"customer_snag": customer_snag})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("home")
