from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    bus_stations = []
    with open(settings.BUS_STATION_CSV, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = [{'Name': rows['Name'], 'Street': rows['Street'], 'District': rows['District']} for rows in reader]

    page_number = request.GET.get('page', 1)
    paginator = Paginator(bus_stations, 3)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'stations/index.html', context)
