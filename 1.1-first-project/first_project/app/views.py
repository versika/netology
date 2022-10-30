from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir, curdir
from os.path import abspath

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/flist.html'
    flist = [filename for filename in listdir(abspath(curdir))]
    return render(request, template_name, {'flist': flist})
