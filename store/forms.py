from django import forms
from .models import *
from django.contrib.auth.models import User


class AddMaterialForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Title", "class": "form-control"}
        ),
        label="",
    )
    inventory = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Inventory", "class": "form-control"}
        ),
        label="",
    )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Details", "class": "form-control"}
        ),
        label="",
    )
    Collection.title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Collection", "class": "form-control"}
        ),
        label="",
    )
    Site.title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Site", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = Material
        fields = (
            "title",
            "inventory",
            "description",
            "collection",
            "site",
        )


class AddCollectionForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Title", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = Collection
        fields = ("title",)
