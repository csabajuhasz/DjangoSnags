from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("customer/<int:pk>", views.customer_snag, name="customer"),
    path("delete_customer/<int:pk>", views.delete_snag, name="delete_customer"),
    path("add_snag/", views.add_snag, name="add_snag"),
    path("update_snag/<int:pk>", views.update_snag, name="update_snag"),
]
