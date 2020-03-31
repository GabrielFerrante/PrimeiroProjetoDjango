#SEM IMPORTAR O ADMIN
from django.urls import path

#importanto as views do app
from .views import viewContato, viewIndex, viewProduto

#Rotas exclusivas para o APP Core
urlpatterns = [
    #rota raiz chama a view index
    path('',viewIndex, name='index'),
    #rota /contato chama a view contato
    path('contato', viewContato, name='contato'),
    #Rota para um produto especifico de acordo com o ID, com o nome da rota produto
    path('produto/<int:id>', viewProduto, name='produto'),
]

