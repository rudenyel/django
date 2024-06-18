import csv
import io
import os
from datetime import datetime, timedelta

from django.shortcuts import render
from faker import Faker
from faker.generator import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.text import slugify

from authors.models import Author
from books.models import Book, Category
from accounts.models import Profile
from project.settings import BASE_DIR, MEDIA_ROOT
from tools.words import animals, adjectives, maxims
from reviews.models import Review
from project.enums import RatingTypes, StatusTypes

fake = Faker()

DELIMITER = ','


def list_view(request):
    template_name = 'tools/list.html'
    return render(request, template_name)


@login_required(login_url=reverse_lazy('accounts:login'))
@user_passes_test(lambda user: user.is_superuser)
def botfarm(request):
    for i in range(10):
        first_name = fake.random.choice(adjectives)
        last_name = fake.random.choice(animals)

        user, created = User.objects.get_or_create(username=last_name)
        if created:
            user.email = f"{first_name}.{last_name}@gmail.com"
            user.set_password('pa$$word')
            user.save()
            profile = Profile.objects.get(user=user)
            profile.first_name = first_name.capitalize()
            profile.last_name = last_name.capitalize()
            profile.phone = f"+420 {fake.msisdn()[4:]}"
            profile.address = fake.address()
            profile.save()

    messages.success(request, 'The bot farm has been successfully created!')
    return HttpResponseRedirect(reverse_lazy('tools:list'))


@login_required(login_url=reverse_lazy('accounts:login'))
@user_passes_test(lambda user: user.is_superuser)
def botfarm_favorites(request):
    users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
    books = Book.published.all()
    for user in users:
        for book in books:
            if fake.boolean(chance_of_getting_true=30):
                if book.favorites.filter(id=user.id):
                    book.favorites.remove(user.id)
                else:
                    book.favorites.add(user.id)
                book.save()
    messages.success(request, 'The bot farm has been successfully created!')
    return HttpResponseRedirect(reverse_lazy('htools:list'))


@login_required(login_url=reverse_lazy('account:login'))
@user_passes_test(lambda user: user.is_superuser)
def botfarm_reviews(request):
    users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
    books = Book.published.all()
    for user in users:
        for book in books:
            if fake.boolean(chance_of_getting_true=30):
                Review.objects.create(
                    book=book, creator=user, editor=user,
                    rating=fake.random.choice(list(RatingTypes)),
                    title=fake.random.choice(maxims),
                    body=fake.paragraph(nb_sentences=5, variable_nb_sentences=True)
                )
    messages.success(request, 'The bot farm has successfully written reviews!')
    return HttpResponseRedirect(reverse_lazy('tools:list'))


@login_required(login_url=reverse_lazy('accounts:login'))
@user_passes_test(lambda user: user.is_superuser)
def upload(request):

    path = f"{BASE_DIR}/{MEDIA_ROOT}"
    authors_images = os.listdir(f"{path}/authors")
    if not authors_images:
        authors_images = ['placeholder.jpg']
    print(authors_images)
    books_images = os.listdir(f"{path}/books")
    if not books_images:
        books_images = ['placeholder.jpg']

    with io.open('upload.csv', encoding='utf-8-sig', mode='r') as file:
        reader = csv.DictReader(file, delimiter=DELIMITER)
        for row in list(reader):

            category_slug = slugify(row['category'])
            category, created = Category.objects.get_or_create(
                name=row['category'], slug=category_slug)
            if created:
                category.status = StatusTypes.PUBLISHED
                category.creator = request.user
                category.editor = request.user
                category.save()

            author_slug = slugify(f"{row['first_name']} {row['last_name']}" if row['first_name'] else row['last_name'])
            author, created = Author.objects.get_or_create(
                surname=row['last_name'], slug=author_slug)
            if created:
                author.name = row['first_name']
                author.born = fake.date_between_dates(
                    date_start=datetime(1900, 1, 1),
                    date_end=datetime(1980, 1, 1))
                if fake.boolean(chance_of_getting_true=70):
                    age = random.randrange(30, 80) * 365 + random.randrange(365)
                    author.died = fake.date_between(author.born, author.born + timedelta(days=age))
                author.occupation = fake.country()
                author.citizenship = fake.country()
                author.biography = fake.paragraph(nb_sentences=6, variable_nb_sentences=True)
                author.status = StatusTypes.PUBLISHED
                author.creator = request.user
                author.editor = request.user
                author.save()
            image = f"{author_slug}.jpg"
            if image not in authors_images:
                image = random.choice(authors_images)
            author.image = f"authors/{image}"
            author.save()

            title_slug = slugify(row['title'])
            book, created = Book.objects.get_or_create(
                title=row['title'], slug=title_slug)
            if created:
                book.description = row['description']
                book.finished = fake.date_between_dates(
                    date_start=datetime(1900, 1, 1),
                    date_end=datetime(1980, 1, 1))
                book.status = StatusTypes.PUBLISHED
                book.creator = request.user
                book.editor = request.user
                book.category = category
                book.authors.add(author)
                book.save()

            image = f"{title_slug}.jpg"
            if image not in books_images:
                image = random.choice(books_images)
            book.image = f"books/{image}"
            book.save()

    messages.success(request, 'The data has been successfully uploaded!')
    return HttpResponseRedirect(reverse_lazy('tools:list'))
