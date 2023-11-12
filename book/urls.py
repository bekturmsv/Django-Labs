from django.urls import path
from .import views

app_name="books"
urlpatterns = [
    # path('', views.view_book),
    # path('book_detail/<int:id>/', views.view_book_detail),
    # path('book_list/', views.view_book_delete),
    # path('book_list/<int:id>/delete/', views.view_book_drop),
    # path('create_book/', views.createViewBookPost),
    # path('add-comment/', views.createReviewForBook),
    path("", views.BookView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view()),
    path('book_list/<int:id>/update/', views.UpdateBookView.as_view()),
    path('create_post_book/', views.CreateBookView.as_view()),
    path('add-comment/', views.createBookReview),
    path('search/', views.SearchView.as_view(), name='search'),
]
