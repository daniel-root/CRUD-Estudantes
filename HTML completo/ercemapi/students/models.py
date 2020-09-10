from django.db import models

class Student(models.Model):
    COURSES = (
        ('Ciência da Computação','Ciência da Computação'),
        ('Fisíca','Fisíca'),
        ('Enfermagem','Enfermagem'),
        ('Engenharia Civil','Engenharia Civil'),
        ('Arquitetura','Arquitetura'),
        ('Química','Química'),
    )
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    city = models.CharField(max_length=30)
    phone = models.IntegerField()
    cpf = models.IntegerField()
    course = models.CharField(max_length=30, choices=COURSES)
    email = models.EmailField()