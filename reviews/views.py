from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from books.models import Book
from reviews.forms import ReviewForm


@login_required(login_url=reverse_lazy('account:login'))
def create_view(request, slug):
    template_name = 'reviews/create.html'
    book = Book.published.get(slug=slug)
    user = request.user
    form = ReviewForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = user
            review.book = book
            review.save()
        return redirect('books:detail', book.slug)

    context = {
        'book': book,
        'form': form,
    }
    return render(request, template_name, context)
