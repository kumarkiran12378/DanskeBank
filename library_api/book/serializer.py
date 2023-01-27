from book.models import Book, Author, Genre
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator


class BookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, validators=[UniqueValidator(Book.objects.all())])
    page_count = serializers.IntegerField()
    release_date = serializers.DateField()
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    authors = serializers.PrimaryKeyRelatedField(allow_empty=True, many=True, queryset=Author.objects.all(), required=False)
    
    class Meta:
        model = Book
    
    def create(self, validated_data):
        authors = validated_data.pop('authors')
        book_instance = Book.objects.create(**validated_data)
        book_instance.authors.add(*authors)
        return book_instance
    
    def update(self, instance, validated_data):
        fields = super().get_fields()
        for field in fields:
            if not fields[field].read_only and field in validated_data:
                try:
                    setattr(instance, field, validated_data[field])
                except TypeError:
                    getattr(instance, field).set(validated_data[field])
        instance.full_clean()
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    author_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    surname = serializers.CharField(max_length=255, required=False)
    email = serializers.CharField(max_length=255, required=True)
    phone = serializers.CharField(max_length=31, required=False)
    facebook_username = serializers.CharField(max_length=255, required=False)
    profile_pic = serializers.ImageField(required=False)
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        validators = [
            UniqueTogetherValidator(
                queryset = Author.objects.all(),
                fields=['name', 'surname']
            )
        ]
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        fields = super().get_fields()
        for field in fields:
            if not fields[field].read_only and field in validated_data:
                try:
                    setattr(instance, field, validated_data[field])
                except TypeError:
                    getattr(instance, field).set(validated_data[field])
        instance.full_clean()
        instance.save()
        return instance

class GenreSerializer(serializers.Serializer):
    genre_id = serializers.IntegerField(read_only=True, required=False)
    name = serializers.CharField(max_length=255, required=False, validators=[UniqueValidator(Genre.objects.all())])

    class Meta:
        model = Genre
    
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
