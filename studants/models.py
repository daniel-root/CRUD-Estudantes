from django.db import models
from datetime import date
# Create your models here.
class Studant(models.Model):
    COURSES = (
        ('Ciência da Computação', 'Ciência da Computação'),
        ('Física', 'Física'),
        ('Enfermagem', 'Enfermagem'),
        ('Engenharia Civil', 'Engenharia Civil'),
        ('Arquitetura', 'Arquitetura'),
        ('Química', 'Química'),
    )
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    course = models.CharField(max_length=50, choices=COURSES)
    email = models.EmailField()
    