from django.shortcuts import render
from .models import ParisEtablissement

def flux_paris(request):
    
    etablissements = ParisEtablissement.objects.all()
    return render(request, "paris/paris_flux.html", context={"etablissements": etablissements})
