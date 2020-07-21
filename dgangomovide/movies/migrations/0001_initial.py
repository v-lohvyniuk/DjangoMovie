# Generated by Django 3.0.8 on 2020-07-21 10:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Вік')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Актори і режисери',
                'verbose_name_plural': 'Актори і режисери',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категорія')),
                ('description', models.TextField(verbose_name='Опис')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Опис')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2000, verbose_name='Дата виходу')),
                ('country', models.CharField(max_length=30, verbose_name='Країна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name="Прем'єра в світі")),
                ('budget', models.PositiveIntegerField(default=0, help_text='Сума в баксах', verbose_name='Бюджет')),
                ('usa_earnings', models.PositiveIntegerField(default=0, help_text='Сума в баксах', verbose_name='Збори в США')),
                ('world_earnings', models.PositiveIntegerField(default=0, help_text='Сума в баксах', verbose_name='Збори в світі')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Чорновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='актор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Category', verbose_name='Категорія')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='режисер')),
                ('genres', models.ManyToManyField(related_name='film_genre', to='movies.Genre', verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'Фільм',
                'verbose_name_plural': 'Фільми',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значення')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('text', models.TextField(max_length=5000, verbose_name='Відгук')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='Фільм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Reviews', verbose_name='Предок')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP Address')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.Movie', verbose_name='Фільм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.RatingStar', verbose_name='Зірка')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(upload_to='movieshots/', verbose_name='Знімок')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='Фільм')),
            ],
            options={
                'verbose_name': 'Кадр з фільму',
                'verbose_name_plural': 'Кадри з фільму',
            },
        ),
    ]
