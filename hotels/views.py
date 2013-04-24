# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Hotel


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotels.html', {'hotels': hotels})
