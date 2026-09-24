from django.urls import path

from . import views

app_name = "music"

urlpatterns = [
    path("", views.index, name="index"),
    path("top-by-country/", views.top_by_country, name="country"),
    path("search/", views.search, name="search"),
    path("charts/", views.charts, name="charts")
]

