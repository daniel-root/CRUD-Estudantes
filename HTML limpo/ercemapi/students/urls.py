from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('Criar/', views.student_create, name='student_create'),
    path('Editar/<int:pk>', views.student_update, name='student_update'),
    path('Ver/<int:pk>', views.student_read, name='student_read'),
    path('Excluir/<int:pk>', views.student_delete, name='student_delete'),
]