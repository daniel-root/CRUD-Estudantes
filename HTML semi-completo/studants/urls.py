from django.urls import path
from . import views

urlpatterns = [
    path('', views.studant_list, name='studant_list'),
    path('Criar', views.studant_create, name='studant_create'),
    path('Ler/<int:studant_id>', views.studant_read, name='studant_read'),
    path('Editar/<int:studant_id>', views.studant_update, name='studant_update'),
    path('Excluir/<int:studant_id>', views.studant_delete, name='studant_delete'),
]