import datetime
from django.core.validators import MinValueValidator
from django.db import models

class News(models.Model):
    """
    Представляет новость, содержащую: 
    title - заголовок новости (обязателен, до 100 символовав)
    short_descreption - краткое описание (до 200 символов)
    description - полное описание новости (до 1000 символов)
    created_date - дата и время создания новости. По умолчанию - текущая дата\время.
    category - категория новости, выбирается из: N: новости U: Обновления
    """
    title = models.CharField(blank=False, max_length=100)
    short_description = models.TextField(blank=False, max_length=200)
    description = models.TextField(blank=False, max_length=2000)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    category = models.CharField(blank=False, max_length=50, choices={"N": "Новости", "U": "Обновления"})


class Goods(models.Model):
    """
    Представляет товар, включающий:
    img - путь или URL к изображению (до 200 символов)
    name - название товара (до 200 символов)
    price - цена товара, должна быть неотрицательной
    description - подробное описание (до 200 символов)
    """
    img = models.CharField(blank=False, max_length=200)
    name = models.CharField(blank=False, max_length=200)
    price = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    description = models.TextField(blank=False, max_length=2000)
