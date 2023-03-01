from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=15)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}{self.pk}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_id': self.pk})