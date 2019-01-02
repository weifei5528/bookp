from django.shortcuts import render
from django.http import HttpResponse

def info(request, id):
    print(id)

    return HttpResponse(id)
    pass