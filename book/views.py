from django.shortcuts import render
from django.views.generic import ListView

from book.models import *


# Create your views here.

def view_book(request):
    queryset = Book.objects.all()
    return render(request, 'books/books.html', {'books': queryset})
