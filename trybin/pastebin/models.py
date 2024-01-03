from django.db import models


class Category(models.Model):
    category_name = models.CharField(blank=True,
                                     unique=True,
                                     max_length=100,
                                     verbose_name="Название категории")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']


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

    PRIVACY_CHOICES = [
        ('Публично', 'Публично'),
        ('Приватно', 'Приватно')
    ]
    privacy = models.CharField(max_length=100,
                               verbose_name='Статус приватности',
                               choices=PRIVACY_CHOICES)

    TIME_TO_TERMINATE = [
        ("Никогда", "Никогда"),
        ('После прочтения', 'После прочтения'),
        ('10 минут', "10 минут"),
        ("1 час", "1 час"),
        ("1 день", "1 день"),
        ("1 неделя", "1 неделя"),
        ("2 недели", "2 недели"),
        ("1 месяц", "1 месяц"),
        ("6 месяцев", "6 месяцев"),
        ("1 год", "1 год"),
    ]
    time_to_delete = models.CharField(max_length=100,
                                      verbose_name='Время удаления поста',
                                      choices=TIME_TO_TERMINATE
                                      )
    is_published = models.BooleanField(default=True,
                                       verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'постов'
        verbose_name_plural = 'Посты'
        ordering = ['-crt_time', 'title']

# Create your models here.
