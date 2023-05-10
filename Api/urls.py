from django.urls import path
from Api.views import BooksApi,BooksApi2

urlpatterns = [
    path('', BooksApi.as_view()),
    path('<str:pk>', BooksApi2.as_view())
]
