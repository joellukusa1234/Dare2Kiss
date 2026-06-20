from django.urls import path
from . import views

urlpatterns = [
    path('', views.salon_jeu, {'room_name': 'principal'}, name='salon_defaut'),
    path('salon/<str:room_name>/', views.salon_jeu, name='salon_jeu'),
]
