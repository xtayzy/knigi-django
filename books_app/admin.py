from django.contrib import admin

from books_app.models import Author, Book

# Register your models here.


admin.site.register([Book, Author])