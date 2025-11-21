from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('cadastrar/', views.cadastrarClientes, name="cadastrarClientes")
]