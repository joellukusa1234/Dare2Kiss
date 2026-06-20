from django.db import models
import uuid

class Categorie(models.Model):
    NOM_CHOICES = [
        ('amical', 'Amical'),
        ('amoureux', 'Amoureux'),
        ('shhhh', 'Shhhh'),
    ]
    nom = models.CharField(max_length=20, choices=NOM_CHOICES, unique=True)

    def __str__(self):
        return self.nom

class Question(models.Model):
    TYPE_CHOICES = [
        ('action', 'Action'),
        ('verite', 'Vérité'),
    ]
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    contenu = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.contenu[:30]}"

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
