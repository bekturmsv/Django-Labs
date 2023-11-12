from django.urls import path
from . import views

urlpatterns = [
    path('cloth/product_list/', views.ProductListView.as_view(), name='product_list'),
    path('cloth/products/men/', views.men_clothing, name='men_clothing'),
    path('cloth/products/women/', views.women_clothing, name='women_clothing'),
    path('cloth/products/kids/', views.kids_clothing, name='kids_clothing'),
    path('cloth/products/unisex/', views.uni_clothing, name='uni_clothing'),
    path('cloth/create_order/', views.CreateOrderView.as_view(),name='create_order'),
    path('cloth/products_by_tag/<str:tag_name>/', views.sort_products_by_tag, name='products_by_tag'),
    path('cloth/error/', views.uni_clothing, name='unisex_clothing'),
    path('cloth/cloth_detail/<int:id>/', views.ClothDetailView.as_view(), name="cloth_detail"),
]
