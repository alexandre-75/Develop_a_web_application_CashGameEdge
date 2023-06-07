from django.shortcuts import render

def province_sectorization(request):
    return render(request, "province/sectorization.html")

def province_north_west(request):
    return render(request, "province/flux_north_west.html")

def province_north_east(request):
    return render(request, "province/flux_north_east.html")

def province_south_west(request):
    return render(request, "province/flux_south_west.html")

def province_south_east(request):
    return render(request, "province/flux_south_east.html")
