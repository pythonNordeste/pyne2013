#coding: utf-8

from .models import Slot
from django.shortcuts import render, redirect


def talk(request, talk_id):
    context = {}
    talk = Slot.objects.filter(id=talk_id, type='talk')
    if talk:
        context['talk'] = talk[0]
        return render(request, 'talk.html', context)
    else:
        return redirect('/')
