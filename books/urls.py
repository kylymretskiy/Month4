from django.urls import path
from . import views

urlpatterns = [
    path('books_list/' , views.books_list),
    path('books_list/<int:id>/' , views.book_detail),
    path('about_me/', views.about_me),
    path('image/', views.image),
    path('time/', views.time),
]


