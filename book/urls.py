from django.urls import path
from .import views

urlpatterns = [
    path('', views.view_book),
    path('book_detail/<int:id>/', views.view_book_detail),
    path('book_list/', views.view_book_delete),
    path('book_list/<int:id>/delete/', views.view_book_drop),
    path('create_book/', views.createViewBookPost),
    path('add-comment/', views.createReviewForBook),
]
