from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.template.context_processors import request

from .models import Book



def about_me(request):
    return HttpResponse("This is the elzat page")

def about_my_pet(request):
    return render(request, 'about_my_pet.html')

def current_time(request):
    return HttpResponse(datetime.datetime.now())

def book_list_view(request):
    if request.method == 'GET':
        books_list = Book.objects.all()
        return render(request, 'book.html', {'books': books_list})


def book_detail_view(request, id):
        book = Book.objects.get(id=id)
        return render(request, 'book_detail.html', {'book': book})