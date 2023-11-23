from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from store.models import *
from django.db.models import Q
from django.contrib import messages
from .forms import AddMaterialForm, AddCollectionForm


# Create your views here.


def collection(request):
    collections = Collection.objects.values(
        "title",
        "update",
        "id",
    )

    return render(request, "store/collection.html", {"collections": collections})


def items_collection(request, pk):
    if request.user.is_authenticated:
        # collections = Collection.objects.get(id=pk).material_set.all()
        collections = get_object_or_404(
            Collection,
            id=pk,
        ).material_set.all()

        # z = collections.material_set.all()

        return render(
            request,
            "store/items_collection.html",
            {"collections": collections},
        )


def add_collection(request):
    form = AddCollectionForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_collection = form.save()
                messages.success(request, f"{add_collection} -- Added")
                return redirect("store/collection")
        return render(request, "store/add_collection.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("snags/home")


def material(request):
    materials = Material.objects.values(
        "title",
        "inventory",
        "description",
        "collection__title",
        "site__title",
        "update",
        "id",
    )

    return render(request, "store/materials.html", {"materials": materials})


def add_material(request):
    form = AddMaterialForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_material = form.save()
                messages.success(request, f"{add_material} -- Added")
                return redirect("store/materials")
        return render(request, "store/add_material.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("snags/home")


def update_material(request, pk):
    if request.user.is_authenticated:
        # current_material = Material.objects.get(id=pk)
        current_material = get_object_or_404(
            Material,
            id=pk,
        )
        form = AddMaterialForm(request.POST or None, instance=current_material)
        if form.is_valid():
            form.save()
            messages.success(request, f"{current_material} -- Has Been Updated")
            return redirect("store/materials")
        return render(request, "store/update_material.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("snags/home")


def search_material(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        # snags = Snag.objects.filter(address__icontains=searched)

        materials = Material.objects.filter(
            Q(title__icontains=searched)
            | Q(collection__title__icontains=searched)
            | Q(site__title__icontains=searched)
        ).distinct()

        return render(
            request,
            "store/search_material.html",
            {"searched": searched, "materials": materials},
        )
    else:
        return render(request, "search.html", {})
