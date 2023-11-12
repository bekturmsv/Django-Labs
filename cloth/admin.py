from django.contrib import admin
from .models import CustomerCL, TagCL, ProductCL, OrderCL

admin.site.register(CustomerCL)
admin.site.register(TagCL)
admin.site.register(ProductCL)
admin.site.register(OrderCL)

