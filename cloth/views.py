from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderForm
from .models import ProductCL,OrderCL,CustomerCL, TagCL
from django.views.generic import *


def men_clothing(request):
    return sort_products_by_tag(request, "men")


def women_clothing(request):
    return sort_products_by_tag(request, "women")


def uni_clothing(request):
    return sort_products_by_tag(request, "uni")


def kids_clothing(request):
    return sort_products_by_tag(request, "kids")


class ProductListView(ListView):
    queryset = ProductCL.objects.filter().order_by('-id')
    template_name = "cloth/product_list.html"

    def get_queryset(self):
        return self.queryset


def sort_products_by_tag(request, tag_name):
    tag = get_object_or_404(TagCL, name=tag_name)
    products = ProductCL.objects.filter(tag=tag)
    context = {"products": products, "tag":tag}
    return render(request, "cloth/products_by_tag.html", context)


def show_error_page(request):
    return render(request, "cloth/error.html")


class CreateOrderView(CreateView):
    model = OrderCL
    form_class = OrderForm
    success_url = "/cloth/product_list"
    template_name = "cloth/create_order.html"


class ClothDetailView(DetailView):
    template_name = "cloth/cloth_detail.html"

    def get_object(self):
        cloth_id = self.kwargs.get("id")
        return get_object_or_404(ProductCL, id=cloth_id)
