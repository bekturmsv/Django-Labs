# Generated by Django 4.2.6 on 2023-10-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='actuality',
            field=models.CharField(choices=[('Актуален', 'Актуален'), ('50 на 50', '50 на 50'), ('Стрем', 'Стрем')], default=('Актуален', 'Актуален'), max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='video',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
