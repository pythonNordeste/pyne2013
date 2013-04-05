#coding: utf-8

from .models import Slot
from django.shortcuts import render, get_object_or_404


def talk(request, talk_id):
    context = {}
    context['talk'] = get_object_or_404(Slot, id=talk_id, type='talk')
    return render(request, 'talk.html', context)
