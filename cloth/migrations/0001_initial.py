# Generated by Django 4.2.6 on 2023-11-12 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TagCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Добавить тэг')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('sex', models.CharField(choices=[('Не указано', 'Не указано'), ('Мужские', 'Мужские'), ('Женские', 'Женские'), ('Универсальные', 'Универсальные'), ('Детские', 'Детские')], default=('Не указано', 'Не указано'), max_length=100)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default=('S', 'S'), max_length=25)),
                ('price', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ManyToManyField(related_name='content_name', to='cloth.tagcl')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloth.customercl')),
                ('products', models.ManyToManyField(to='cloth.productcl')),
            ],
        ),
    ]
