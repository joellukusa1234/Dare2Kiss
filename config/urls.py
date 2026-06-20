from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jeu/', include('jeu.urls')), # On branche notre app ici
]
