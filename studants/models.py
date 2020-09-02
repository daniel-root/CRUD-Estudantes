from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
def validate_even(value):
    if int(value) % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
class Studant(models.Model):
    COURSES = (
        ('Ciência da Computação', 'Ciência da Computação'),
        ('Física', 'Física'),
        ('Enfermagem', 'Enfermagem'),
        ('Engenharia Civil', 'Engenharia Civil'),
        ('Arquitetura', 'Arquitetura'),
        ('Química', 'Química'),
    )
    name = models.CharField('Nome',max_length=30)
    birth_date = models.DateField('Data  de Nasimento')
    city = models.CharField('Cidade',max_length=50,default="Viçosa do Ceará")
    phone = models.CharField('Telefone',max_length=11)
    cpf = models.CharField('CPF',max_length=11,validators=[validate_even])
    course = models.CharField('Curso',max_length=50, choices=COURSES)
    email = models.EmailField('E-mail')
    
    