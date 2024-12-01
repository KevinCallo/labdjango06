from django import forms
from .models import User, Book, Review

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'book', 'review_text']
