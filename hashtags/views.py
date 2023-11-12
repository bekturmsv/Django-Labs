from django.shortcuts import get_object_or_404
from .models import Tag, Product
from django.views import generic

class ProductView(generic.ListView):
    queryset = Product.objects.filter().order_by("-id")
    template_name = "hashtags/product.html"

    def get_queryset(self):
        return self.queryset

# class MusicHashtagsViews(generic.ListView):
#     queryset = Product.objects.filter(tag__name='Музыка')
#     template_name = "hashtags/product_music.html"
#
#     def get_queryset(self):
#         return self.queryset

class ProductDetailView(generic.DetailView):
    template_name = "hashtags/product_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id = product_id)