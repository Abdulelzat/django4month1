from django.shortcuts import render
from django.http import HttpResponse
import datetime
def about_me(request):
    return HttpResponse("This is the elzat page")

def about_my_pet(request):
    return render(request, 'about_my_pet.html')

def curent_time(request):
    return HttpResponse(datetime.datetime.now())