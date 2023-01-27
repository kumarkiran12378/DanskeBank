from django.contrib import admin
from django.urls import path, include
from book.views import BookViewSet, AuthorViewSet, GenreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')
router.register('books', BookViewSet, basename='book')
router.register('authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('/', include(router.urls)),
]
