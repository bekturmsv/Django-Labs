# Generated by Django 4.2.6 on 2023-10-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_reviewbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='actuality',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Жанр', 'Жанр'), ('Боевик', 'Боевик'), ('Романтика', 'Романтика')], default=('Жанр', 'Жанр'), max_length=100, null=True),
        ),
    ]
