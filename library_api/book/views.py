
from django_filters import rest_framework, FilterSet
from rest_framework import viewsets
from book.models import Book, Author, Genre
from book.serializer import BookSerializer, AuthorSerializer, GenreSerializer
from book.filters import AuthorFilter, BookFilter
from user.permission import IsAuthenticatedLibrarian


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ('get', 'post', 'delete')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = BookFilter
    permission_classes = [IsAuthenticatedLibrarian]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = AuthorFilter
    permission_classes = [IsAuthenticatedLibrarian]
