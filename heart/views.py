from django.http import HttpResponse
from django.shortcuts import render


def classify_image(request):
    return render(request, 'classify.html')
