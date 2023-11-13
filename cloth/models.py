from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100, verbose_name="Добавить тэг")

    def __str__(self):
        return f'#{self.name}'


class ProductCL(models.Model):
    SEX = (
        ("Not Indicated", "Not Indicated"),
        ("men", "men"),
        ("women", "women"),
        ("uni", "uni"),
        ("kids", "kids")
    )

    SIZES = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
        ("All sizes available", "All sizes available")
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=100, choices=SEX, default=SEX[0])
    size = models.CharField(max_length=25, choices=SIZES, default=SIZES[0])
    price = models.CharField(max_length=20)
    tag = models.ManyToManyField(TagCL, related_name="content_name")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}--{self.created_at}'


class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCL)
    order_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order {self.pk if self.pk else 'New order'} by {self.customer.name} "
