from django.shortcuts import render
from django.views import generic
from . import models

class AllCategoryBooksView(generic.ListView):
    template_name = 'tags/all_category_book.html'
    context_object_name = 'query'
    model = models.Product

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all()

# def all_category_book(request):
#     if request.method == 'GET':
#         query = models.Product.objects.all()
#         return render(request,
#                       template_name='tags/all_category_book.html',
#                       context={'query': query}
#                       )
class TeenBooksView(generic.ListView):
    template_name = 'tags/teen_category_book.html'
    context_object_name = 'query'
    model = models.Product

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().filter(tags__name='Для подростков')

# def teen_category_book(request):
#     if request.method == 'GET':
#         query = models.Product.objects.all().filter(tags__name='Книги для подростков')
#         return render(request,
#                       template_name='tags/teen_category_book.html',
#                       context={'query': query}
#                       )
class KidsBooksView(generic.ListView):
    template_name = 'tags/kids_category_book.html'
    context_object_name = 'query'
    model = models.Product

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().filter(tags__name='Для детей')

# def kids_category_book(request):
#     if request.method == 'GET':
#         query = models.Product.objects.all().filter(tags__name='Книги для детей')
#         return render(request,
#                       template_name='tags/kids_category_book.html',
#                       context={'query': query})
