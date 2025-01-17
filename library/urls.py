from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me , name='about_me'),
    path('about_my_pet/' , views.about_my_pet, name='about_my_pet'),
    path('curent_time/', views.curent_time , name='curent_time'),
]
