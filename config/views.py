from django.http import HttpResponse

def index(request):
    return HttpResponse('Вітаю! Це головна сторінка')