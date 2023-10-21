from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms



# Create your views here.

def view_book(request):
    book_value = models.Book.objects.all()
    return render(request,"books/books.html",{"book_key" : book_value})

def view_book_detail(request, id):
    book_id = get_object_or_404(models.Book, id = id)
    return render(request, 'books/book_detail.html', {'book_key' : book_id})

def createViewBookPost(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен')
    else:
        form = forms.BookForm()
    return render(request, 'books/create_book.html', {'form': form})

def view_book_delete(request):
    lang_value = models.Book.objects.all()
    return render(request, 'books/book_list.html', {'lang_key': lang_value})

def view_book_drop(request, id):
    lang_id = get_object_or_404(models.Book, id=id)
    lang_id.delete()
    return HttpResponse('Успешно удален')

def createReviewForBook(requset):
    method = requset.method
    if method == 'POST':
        form = forms.ReviewForm(requset.POST, requset.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse('<h1>Success</h1>')
    else:
        form = forms.ReviewForm()

    return render(requset, 'books/createReview.html', {'form' : form})