from django import forms
from app.models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        book = BookModel
        fields = ['title', 'author', 'published_date']
