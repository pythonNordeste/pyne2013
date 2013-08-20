#encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect

from .models import Enrollment
from .forms import SearchEnrollmentForm

def download(request):
    form = SearchEnrollmentForm(data=request.POST or None)
    context = {}
    enrollments = None
    if form.is_valid():
        enrollments = form.enrollments()
    context = {
        'enrollments': enrollments,
        'form': form,
    }
    return render(request, 'certificates/download.html', context)