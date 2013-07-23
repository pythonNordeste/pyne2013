# -*- coding: utf-8 -*-
from django.shortcuts import render


def course_list(request):
    return render(request, 'courses/courses.html', {})
