"""projeto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#ARQUIVO DE ROTAS
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from core import views

#Sempre chamamos funções das views

#Incluir as urls expecificas de cada app
urlpatterns = [
    #Ferramenta Administrativa
    path('painel/', admin.site.urls),
    #Toda vez que cair na raiz do site, ir para as urls da app core
    path('', include('core.urls')),
]



#Melhorando o erro 404
#SETANDO A VIEW DE ERROS
handler404 = views.view404
#Melhorando o erro 500
handler500 = views.view500