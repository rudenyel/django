from django.shortcuts import render

from authors.models import Author


def list_view(request):
    template_name = 'authors/list.html'
    authors = Author.published.all()
    context = {
        'authors': authors,
    }
    return render(request, template_name, context)


def detail_view(request, slug):
    template_name = 'authors/detail.html'
    author = Author.published.get(slug=slug)
    context = {
        'author': author,
    }
    return render(request, template_name, context)
