from django.db import models


class Author(models.Model):
    """
    Author Model.
    """
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=31, null=True, blank=True)
    facebook_username = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'author'
        constraints = [
            models.UniqueConstraint(name='unique_name', fields=['name', 'surname'])
            ]

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'genre'


class Book(models.Model):
    """
    Book model.
    """
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    page_count = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='book_list')
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'book'


