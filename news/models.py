from django.db import models

# Create your models here.


class Articles(models.Model):
    #author = models.CharField('Автор', max_length=150)
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
