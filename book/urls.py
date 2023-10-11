from django.urls import path
from book.views import *

urlpatterns = [
    path('', view_book),
]
