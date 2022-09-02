from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def hi(request):
    return render(request, 'FIRSTWEBSITE/hi.html')
