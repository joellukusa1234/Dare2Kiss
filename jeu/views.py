from django.shortcuts import render
from .models import Categorie

def salon_jeu(request, room_name):
    categories = Categorie.objects.all()
    return render(request, 'jeu/salon.html', {
        'room_name': room_name,
        'categories': categories
    })