from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def history(request):
    return render(request, 'main/history.html')

def excursus(request):
    return render(request, 'main/excursus.html')

def nature(request):
    return render(request, 'main/nature.html')