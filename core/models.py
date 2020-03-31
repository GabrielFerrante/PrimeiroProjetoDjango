#Só aplicações tem models
#Models servem para persistir dados
#Criamos classes aqui e o django gera um modelo de banco de dados

#Sempre confirme no settings se o app ta instalado 
from django.db import models

#Criando uma model
#Sempre herdar da classe Model
class Produto(models.Model):
    #atributos
    #O primeiro campo sempre é um atalho ou apelido
    #Para String
    nome = models.CharField('Nome',max_length=100)
    #Para decimais
    #decimal_ places é a quantidade de casas
    preco = models.DecimalField('Preço',decimal_places=2, max_digits=8)
    #Para inteiros
    estoque = models.IntegerField('Quantidade em Estoque')

    #Ela apresenta o objeto instaciado pelo nome
    def __str__(self):
        #montando uma string com os atributos
        return f'{self.nome} / Estoque: {self.estoque}'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome ', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

    