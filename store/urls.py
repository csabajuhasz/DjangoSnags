from django.urls import path
from . import views


urlpatterns = [
    path("collection", views.collection, name="store/collection"),
    path("add_collection/", views.add_collection, name="store/add_collection"),
    path(
        "items_collection/<int:pk>",
        views.items_collection,
        name="store/items_collection",
    ),
    path("materials", views.material, name="store/materials"),
    path("add_material/", views.add_material, name="store/add_material"),
    path(
        "update_material/<int:pk>", views.update_material, name="store/update_material"
    ),
    path("search_material", views.search_material, name="store/search_material"),
]
