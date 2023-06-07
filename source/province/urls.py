from django.urls import path
from . import views

urlpatterns = [
    path("", views.province_sectorization, name="province_province_sectorization"),
    path("north_west/", views.province_north_west, name="province_province_north_west"),
    path("north_east/", views.province_north_east, name="province_province_north_east"),
    path("south_west/", views.province_south_west, name="province_province_south_west"),
    path("south_east/", views.province_south_east, name="province_province_south_east"),
]