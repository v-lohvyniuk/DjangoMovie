from django.db import models
from datetime import date


class Category(models.Model):

    name = models.CharField("Категорія", max_length=150)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Actor(models.Model):

    name = models.CharField("Ім'я", max_length=100)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    description = models.TextField("Опис")
    image = models.ImageField("Фото", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актори і режисери"
        verbose_name_plural = "Актори і режисери"


class Genre(models.Model):

    name = models.CharField("Назва", max_length=150)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Movie(models.Model):

    title = models.CharField("Назва", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Опис")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата виходу", default=2000)
    country = models.CharField("Країна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режисер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актор", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанр", related_name="film_genre")
    world_premiere = models.DateField("Прем'єра в світі", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Сума в баксах")
    usa_earnings = models.PositiveIntegerField("Збори в США", default=0, help_text="Сума в баксах")
    world_earnings = models.PositiveIntegerField("Збори в світі", default=0, help_text="Сума в баксах")
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Чорновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"


class MovieShots(models.Model):

    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Опис")
    image = models.ImageField("Знімок", upload_to="movieshots/")
    movie = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр з фільму"
        verbose_name_plural = "Кадри з фільму"


class RatingStar(models.Model):

    value = models.PositiveSmallIntegerField("Значення", default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):

    ip = models.CharField("IP Address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Зірка")
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name="Фільм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=100)
    text = models.TextField("Відгук", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Предок", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
