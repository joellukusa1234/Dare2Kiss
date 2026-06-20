from django.urls import path
from . import views

urlpatterns = [
    path('salon/<str:room_name>/', views.salon_jeu, name='salon_jeu'),
]