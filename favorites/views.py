from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from books.models import Book


@login_required
def list_view(request):
    template_name = 'favorites/list.html'
    user = request.user
    books = Book.published.filter(favorites=user)
    context = {
        'books': books,
    }
    return render(request, template_name, context)


@login_required
def ajax_toggle_view(request, slug):
    book = Book.published.get(slug=slug)
    created = True
    if book.favorites.filter(id=request.user.pk):
        book.favorites.remove(request.user)
        created = False
    else:
        book.favorites.add(request.user)
    book.save()
    return JsonResponse({'favorite': created})


@login_required
def toggle_view(request, slug):
    book = Book.published.get(slug=slug)
    if book.favorites.filter(id=request.user.pk):
        book.favorites.remove(request.user)
    else:
        book.favorites.add(request.user)
    book.save()
    return HttpResponseRedirect(reverse_lazy('favorites:list'))
