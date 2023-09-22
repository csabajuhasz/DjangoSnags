from django.urls import path
from . import views


urlpatterns = [
    path("", views.operatives, name="operatives/home"),
    path(
        "operatives/<int:pk>",
        views.individual,
        name="operatives/individual",
    ),
    path("operatives/", views.job, name="operatives/detail"),
    # path("search_job", views.search_job, name="operatives/search_job"),
]
