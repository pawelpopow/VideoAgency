from django.shortcuts import render


def world_map(request):
    return render(request, "map/maps.html")
