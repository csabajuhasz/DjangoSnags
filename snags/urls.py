from django.urls import path
from . import views

# app_name = "snags"

urlpatterns = [
    path("", views.core, name="core"),
    path("home/", views.home, name="snags/home"),
    path("snag_list/", views.snag_list, name="snags/snag_list"),
    path("logout/", views.logout_user, name="snags/logout"),
    path("register/", views.register_user, name="snags/register"),
    path("customer/<int:pk>", views.customer_snag, name="snags/customer"),
    path("delete_customer/<int:pk>", views.delete_snag, name="snags/delete_customer"),
    path("add_snag/", views.add_snag, name="snags/add_snag"),
    path("update_snag/<int:pk>", views.update_snag, name="snags/update_snag"),
    path("search", views.search, name="search"),
    path("snag_csv", views.snag_csv, name="snag_csv"),
    path("admin_snag_pdf/<int:pk>", views.admin_snag_pdf, name="snags/pdf"),
]
