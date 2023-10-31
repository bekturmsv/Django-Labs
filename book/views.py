from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


# Create your views here.

class BookView(generic.ListView):
    book_value = models.Book.objects.all()
    template_name = "books/book_list.html"

    def get_queryset(selfs):
        return models.Book.objects.all()

# def view_book(request):
#     book_value = models.Book.objects.all()
#     return render(request,"books/books.html",{"book_key" : book_value})

class BookDetailView(generic.DetailView):
    template_name = "books/book_detail.html"

    def get_object(self):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def view_book_detail(request, id):
#     book_id = get_object_or_404(models.Book, id = id)
#     return render(request, 'books/book_detail.html', {'book_key' : book_id})

class CreateBookView(generic.CreateView):
    template_name = "books/create_book.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)

# def createViewBookPost(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен')
#     else:
#         form = forms.BookForm()
#     return render(request, 'books/create_book.html', {'form': form})


class UpdateBookView(generic.UpdateView):
    template_name = "books/update_book.html"
    form_class = forms.BookForm
    success_url = "/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        return super(UpdateBookView, self).form_valid(form=form)

# def view_book_delete(request):
#     lang_value = models.Book.objects.all()
#     return render(request, 'books/book_list.html', {'lang_key': lang_value})


class BookDropView(generic.DeleteView):
    template_name = "books/confirm_book_delete.html"
    success_url = "/"

    def get_object(self, queryset=None):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

def createBookReview(request):
    method = request.method
    if(method == "POST"):
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Успешно добавлен</h1>")
    else:
        form = forms.ReviewForm()

    return render(request, "books/createReview.html",{"form": form})

class SearchView(generic.ListView):
    template_name = "books/book_list.html"
    context_object_name = "book"
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q")
        return context
# def view_book_drop(request, id):
#     lang_id = get_object_or_404(models.Book, id=id)
#     lang_id.delete()
#     return HttpResponse('Успешно удален')
#
# def createReviewForBook(requset):
#     method = requset.method
#     if method == 'POST':
#         form = forms.ReviewForm(requset.POST, requset.FILES)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponse('<h1>Success</h1>')
#     else:
#         form = forms.ReviewForm()
#
#     return render(requset, 'books/createReview.html', {'form' : form})