from django.shortcuts import render

from books.models import Book


def list_view(request):
    template_name = 'books/list.html'
    books = Book.published.all()
    context = {
        'books': books,
    }
    return render(request, template_name, context)


def detail_view(request, slug):
    template_name = 'books/detail.html'
    book = Book.published.get(slug=slug)
    context = {
        'book': book,
    }
    return render(request, template_name, context)
