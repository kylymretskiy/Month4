from django.urls import path
from . import views

urlpatterns = [
    path('all_tags_films/', views.all_category_book, name='all'),
    path('teen_tags_films/', views.teen_category_book, name='teen'),
    path('kids_tags_films/', views.kids_category_book, name='kids'),
]