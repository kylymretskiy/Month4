from django.shortcuts import render
from . import models


def all_category_book(request):
    if request.method == 'GET':
        query = models.Product.objects.all()
        return render(request,
                      template_name='tags/all_category_book.html',
                      context={'query': query}
                      )
def teen_category_book(request):
    if request.method == 'GET':
        query = models.Product.objects.all().filter(tags__name='Книги для подростков')
        return render(request,
                      template_name='tags/teen_category_book.html',
                      context={'query': query}
                      )
def kids_category_book(request):
    if request.method == 'GET':
        query = models.Product.objects.all().filter(tags__name='Книги для детей')
        return render(request,
                      template_name='tags/kids_category_book.html',
                      context={'query': query})
