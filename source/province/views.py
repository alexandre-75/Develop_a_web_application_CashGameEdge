from django.shortcuts import render
from .models import ProvinceEtablissement

def province_sectorization(request):
    return render(request, "province/sectorization.html")

def province_north_west(request):
    nw = ProvinceEtablissement.objects.filter(province="NW")
    return render(request, "province/flux_north_west.html", context={"nw":nw})

def province_north_east(request):
    ne = ProvinceEtablissement.objects.filter(province="NE")
    return render(request, "province/flux_north_east.html", context={"ne":ne})

def province_south_west(request):
    sw = ProvinceEtablissement.objects.filter(province="SW")
    return render(request, "province/flux_south_west.html", context={"sw":sw})

def province_south_east(request):
    se = ProvinceEtablissement.objects.filter(province="SE")
    return render(request, "province/flux_south_east.html", context={"se":se})
