from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class PositionSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            degree = request.POST.get('degree')
            if not degree:
                return HttpResponseBadRequest("Необходимо указать диплом")

            if degree == "bachelor":
                request.position = "Библиотекарь"
                request.salary = 20000
            elif degree == "master":
                request.position = "Главный библиотекарь"
                request.salary = 40000
            elif degree == "docent":
                request.position = "Директор"
                request.salary = 60000
            else:
                request.position = "уборщица"
                request.salary = 17000