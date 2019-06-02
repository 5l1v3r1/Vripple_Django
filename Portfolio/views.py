from django.http import HttpResponse
from django.shortcuts import render


def portfolio(request):
    return render(request, "Portfolio.html")