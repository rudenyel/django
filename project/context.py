from books.models import Category


def menu(request):
    categories = Category.published.values('name', 'slug')
    return {'categories': categories}
