from django.shortcuts import render, redirect


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_date_view(request, pub_date):
    template = 'books/books_list.html'