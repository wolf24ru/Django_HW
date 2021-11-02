from models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    # TODO Придумтаь как отсортировать полученый объект
    match sort:
        case 'name':
            ...
        case 'cheap':
            ...
        case 'expensive':
            ...
        case _:
            ...
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__iexact=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
