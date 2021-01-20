from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'abstract', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Название статьи',
                'class': 'form-control'
            }),
            "abstract": TextInput(attrs={
                'placeholder': 'Аннотация',
                'class': 'form-control'
            }),
            "full_text": Textarea(attrs={
                'placeholder': 'Текст статьи',
                'class': 'form-control'
            }),
            "date": DateTimeInput(attrs={
                'placeholder': 'Дата публикации (YYYY-MM-DD HH:MM:SS)',
                'class': 'form-control',
                'type': 'datetime-local'
            })
    }