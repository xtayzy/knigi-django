from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books_app import views

router = DefaultRouter()

router.register(r'books', views.BookViewSet, basename='books')
router.register(r'authors', views.AuthorViewSet, basename='authors')

urlpatterns = [
    path('', include(router.urls))
]