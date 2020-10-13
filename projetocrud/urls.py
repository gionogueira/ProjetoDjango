from django.urls import path
from . import views

urlpatterns = [
    path('', views.listcliente, name='listcliente'),
    path('cadastro/', views.cadastrocliente, name='cadastrocliente'),
    path('editar/<int:pk>/', views.editcliente, name='editcliente'),
    path('deletar/<int:pk>/', views.deletcliente, name='deletcliente'),
]
