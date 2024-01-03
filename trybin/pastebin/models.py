from django.db import models


class Category(models.Model):
    category_name = models.CharField(blank=True,
                                     unique=True,
                                     max_length=100,
                                     verbose_name="Название категории")


class NewPost(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок поста')
    text = models.TextField(blank=True,
                            verbose_name='Текст поста')
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория')
    tags = models.CharField(max_length=100,
                            verbose_name='Теги')
    crt_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Время создания')





# Create your models here.
