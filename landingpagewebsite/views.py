from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = '<h1>Прифет притурки!</h1>'
    text = 'Новый текст'
    # return HttpResponse(a)
    return render(request, './index.html', {
        'a': a,
        'text': text
    })