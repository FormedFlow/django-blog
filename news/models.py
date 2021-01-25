from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField('Заголовок', max_length=50)
    abstract = models.CharField('Аннотация', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
