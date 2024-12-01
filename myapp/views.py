from django.shortcuts import render, redirect
from .forms import UserForm, BookForm, ReviewForm
from .models import User, Book, Review

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def home(request):
    users = User.objects.all()
    books = Book.objects.all()
    reviews = Review.objects.all()
    return render(request, 'home.html', {'users': users, 'books': books, 'reviews': reviews})
