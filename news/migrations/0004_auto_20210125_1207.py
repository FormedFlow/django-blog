# Generated by Django 3.1.5 on 2021-01-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(max_length=150, verbose_name='Автор'),
        ),
    ]
