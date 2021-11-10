from .models import Book
from django.shortcuts import render, redirect
from books.castompaginator import IterPaginator


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def books_date_view(request, pub_date_req: str):
    template = 'books/books_date.html'
    objects_list = Book.objects.all()
    date_books = []
    paginator_dict = {}

    for book in objects_list.order_by('pub_date'):
        paginator_dict.update({str(book.pub_date): objects_list.filter(pub_date=book.pub_date)})
        if book.pub_date not in date_books:
            date_books.append(str(book.pub_date))
    iter_paginator = IterPaginator(date_books, pub_date_req)

    context = {
        'nex_date': iter_paginator.next(),
        'prev_date': iter_paginator.prev(),
        'books': paginator_dict[pub_date_req],
    }
    return render(request, template, context)
