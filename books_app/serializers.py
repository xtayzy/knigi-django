from rest_framework import serializers

from books_app.models import Book, Author


class SerializerBook(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = 'title', 'image', 'details'


class AuthorSerializer(serializers.ModelSerializer):
    books = SerializerBook(many=True)

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

