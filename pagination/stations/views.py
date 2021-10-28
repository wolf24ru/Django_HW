import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    # print(settings.BUS_STATION_CSV)
    with open(settings.BUS_STATION_CSV) as cvs_bus:
        dict_bus_lifo = list(csv.DictReader(cvs_bus))
        bus_paginator = Paginator(dict_bus_lifo, 10)
    current_page = request.GET.get('page', 1)
    page = bus_paginator.get_page(current_page)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
