from django.shortcuts import render

from books.models import Book, Category


def list_view(request):
    template_name = 'books/list.html'
    books = Book.published.all()
    context = {
        'books': books,
        'category': 'Books'
    }
    return render(request, template_name, context)


def category_view(request, slug):
    template_name = 'books/list.html'
    books = Book.published.filter(category__slug__contains=slug)
    category = Category.published.get(slug=slug)
    context = {
        'books': books,
        'category': category
    }
    return render(request, template_name, context)


def detail_view(request, slug):
    template_name = 'books/detail.html'
    book = Book.published.get(slug=slug)
    context = {
        'book': book,
    }
    return render(request, template_name, context)

