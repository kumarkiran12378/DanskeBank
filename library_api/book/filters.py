
import django_filters
from book.models import Book, Author


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = {
            'title':[],
            'page_count':['exact', 'gt', 'lt'],
            'release_date': ['exact', 'gt', 'lt'],
            'authors': ['exact']
        }


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    surname = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = {
            'author_id': ('exact',),
            'name': [],
            'surname': [],
            'email': []
        }
