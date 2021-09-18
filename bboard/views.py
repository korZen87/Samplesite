from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb

def index(request):
    s='Список объявлений\n\n\n\n'
    for bb in Bb.objects.order_by('-published'):
        s+=bb.title+'\n'+bb.content+'\n\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

