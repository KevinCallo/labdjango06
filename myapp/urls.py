from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_review/', views.add_review, name='add_review'),
]
