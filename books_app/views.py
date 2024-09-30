from msilib.schema import ListView

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from books_app.models import Book, Author
from books_app.serializers import BookSerializer, AuthorSerializer


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Book.objects.all()
        filter_item = self.request.query_params.get('order_by')
        if filter_item == 'nurik':
            return queryset
        if filter_item is not None:
            queryset = queryset.order_by(filter_item)

        return queryset


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Author.objects.all()
        filter_item = self.request.query_params.get('order_by')

        if filter_item == 'nurik':
            return queryset
        if filter_item is not None:
            queryset = queryset.order_by(filter_item)

        return queryset

