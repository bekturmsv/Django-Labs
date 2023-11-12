from django.urls import path
from . import views

urlpatterns = [
    path('product_tags/',views.ProductView.as_view()),
    path('product_tags/<int:id>/', views.ProductDetailView.as_view()),
    # path('product_music_tags/', views.MusicHashtagsViews.as_view()),
]