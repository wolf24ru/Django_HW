from .models import Book
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def books_date_view(request, pub_date_req):
    template = 'books/books_date.html'
    objects_list = Book.objects.all()
    date_books = []
    paginator_dict = {}
    # current_books = objects_list.filter(pub_date=pub_date)
    for book in objects_list.order_by('pub_date'):
        paginator_dict.update({book.pub_date: objects_list.filter(pub_date=book.pub_date)})
        if book.pub_date not in date_books:
            date_books.append(book.pub_date)
    #TODO сделать пангинатор из имеющихся данных.

    # date_list = [i.pub_date for i in objects_list]
    # paginator = Paginator(paginator_dict, 1)
    # current_page = request.GET.get('page', pub_date_req)
    # page = paginator.get_page(current_page)
    context = {
        # 'page': page,
        # 'books': page.object_list,
    }
    return render(request, template, context)