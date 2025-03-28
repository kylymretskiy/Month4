from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import generic
from . import models, forms

class JanmatesBooksListView(generic.ListView):
    template_name = 'parser/janmate_film_list.html'
    context_object_name = 'janmate'
    model = models.JanmatesBooksModel

    def get_queryset(self):
        return models.JanmatesBooksModel.objects.all()

#Общая форма не зависимо от того сколько у нас сайтов для парсинга
class ParserForm(generic.FormView):
    template_name = 'parser/parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Парсинг успешно завершен</h1>')
        else:
            return super(ParserForm, self).post(request, *args, **kwargs)
