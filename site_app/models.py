import datetime

from django.contrib.auth.models import User
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
    created_date = models.DateTimeField(auto_now_add=True)


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
    # categories
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='avatars/', blank=True,null = True)
    description = models.TextField(blank=False, max_length=2000)
class Reviews(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=2000)
    stars = models.IntegerField(validators=[MinValueValidator(1)])
    def __str__(self):
        return self.title
class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=2000)
    img = models.ImageField(upload_to='forumImg/', blank=True,null = True)
    is_closed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bind_to_ask = models.ForeignKey(Forum, on_delete=models.CASCADE)
    description = models.TextField(blank=False, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description
