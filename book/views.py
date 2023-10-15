from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from book.models import *


# Create your views here.

def view_book(request):
    queryset = Book.objects.all()
    return render(request, 'books/books.html', {'books': queryset})


def view_book_detail(request, id):
    lang_id = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'lang_key': lang_id})
