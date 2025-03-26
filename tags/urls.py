from django.urls import path
from . import views

urlpatterns = [
    path('all_tags_films/', views.AllCategoryBooksView.as_view(), name='all'),
    path('teen_tags_films/', views.TeenBooksView.as_view(), name='teen'),
    path('kids_tags_films/', views.KidsBooksView.as_view(), name='kids'),

]