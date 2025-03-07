from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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

