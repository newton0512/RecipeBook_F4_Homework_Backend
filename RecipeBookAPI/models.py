from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    img = models.ImageField(upload_to='media/images')
    content = models.TextField()


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    img = models.ImageField(upload_to='media/images')
    # внешний ключ
    cat_id = models.ForeignKey(Category, models.CASCADE)
