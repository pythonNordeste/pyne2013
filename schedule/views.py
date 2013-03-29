#coding: utf-8

from .models import Slot
from django.shortcuts import render


def talk(request, talk_id):
    context = {}
    context['talk'] = Slot.objects.get(id=talk_id)
    return render(request, 'talk.html', context)
