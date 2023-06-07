from django.urls import path
from . import views

urlpatterns = [
    path("", views.flux_paris, name="paris_flux_paris")
]