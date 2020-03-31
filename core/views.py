#FUNCOES CHAMADAS PELAS ROTAS PARA ABRIR TEMPLATES

#Atalhos do Django
from django.shortcuts import render, get_object_or_404
#Para gerar respostas HTTP
from django.http import HttpResponse

from django.template import loader
#Models
from .models import Produto

#Views sempre recebem uma request
#Elas só existem em aplicações
def viewIndex(request):
    
    produtos = Produto.objects.all()

    #passando dados para um template
    context = {
        'curso': 'Programação com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    #Retorna uma renderização do template index.html
    return render(request,'index.html',context)

def viewContato(request):
    return render(request, 'contato.html')

def viewProduto(request, id):
    #print(f'ID DO PRODUTO: {id}')
    #produto = Produto.objects.get(id = id)
    produto = get_object_or_404(Produto, id=id)
    #print(f'NOME: {produto.nome}')
    context = {
       'nome':produto.nome,
       'preco':produto.preco,
       'estoque':produto.estoque
    }
    return render(request, 'produto.html',context)

#VIEWS ESPECÍFICAS PARA ERROS
def view404(request, EXCEPTION):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)

def view500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)