
from django.contrib import admin
#importando as models para registrar na administração do Django
from .models import Cliente, Produto

#Mostrando outros campos do model na administração

class ProdutoAdmin(admin.ModelAdmin):
    #os campos deve corresponder ao nome dos atributos
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome', 'email')


#Registrar na administração as models + classe de personalização
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)


