from django.shortcuts import render

def flux_paris(request):
    return render(request, "paris/paris_flux.html")
