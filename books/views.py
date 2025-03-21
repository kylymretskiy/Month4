from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic, View
from . import models


class SearchBooksView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)

# def book_detail(request,id):
#     if request.method == "GET":
#         book_id = get_object_or_404(models.Books, id=id)
#         return render(
#             request,
#             template_name='book_detail.html',
#             context={
#                 'book_id': book_id,
#             }
#         )

class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'
    model = models.Books

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all()

# def books_list(request):
#     if request.method == "GET":
#         query = models.Books.objects.all()
#         return render(
#             request,
#             template_name='book.html',
#             context={
#                 'query': query,
#             }
#         )


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Кылымбек. Я обучаюсь в Политехе КГТУ по специальности «Техническое обслуживание средств вычислительной техники». Помимо учебы, активно изучаю программирование: прошел практику на курсах Geeks, освоил основы Python и ООП, а также начал разрабатывать Telegram-ботов с использованием Aiogram.Также интересуюсь цифровой логикой и работаю в Logisim-Evolution.Стремлюсь развиваться в IT-сфере, углубляя свои знания и навыки в программировании.")

def image(request):
    if request.method == "GET":
        return HttpResponse("<img src='https://static.sobaka.ru/images/image/01/63/21/50/_normal.jpeg?v=1671365310'> Pushok")

def time(request):
    if request.method == "GET":
        now = datetime.now().strftime("%H:%M:%S")
        return HttpResponse(f"{now}")

