from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me , name='about_me'),
    path('about_my_pet/' , views.about_my_pet, name='about_my_pet'),
    path('curent_time/', views.current_time , name='curent_time'),

    path('book/', views.book_list_view, name='book_list_view'),
    path('book/<int:id>/', views.book_detail_view, name='book_detail_view'),
]
