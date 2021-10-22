from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from os import listdir
# Create your views here.


def home(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_item(request):
    time_now = datetime.now().time()
    msg = f'<h3>Текущее время в Красноярске:</h3> \n<h1>{time_now.strftime("%H:%M:%S")}</h1>' \
          f'<a href="{reverse("home")}">Вернуться на главную </a>' \
          f'<script type="text/javascript">setTimeout(()=>location.reload(),1000)</script>'
    return HttpResponse(msg)


def workdir(request):
    template_name = 'app/workdir.html'
    path_list = [f for f in listdir('./')]
    context = {
        'path_list': path_list,
        'home_url': reverse('home')
    }
    return render(request, template_name, context)
