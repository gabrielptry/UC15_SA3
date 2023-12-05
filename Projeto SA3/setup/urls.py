"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from tasks.views import pagina_inicial
from tasks.views import lista_tarefa
from tasks.views import pagina_sobre
from tasks.views import cadastros

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", pagina_inicial, name = "home"),
    path("tarefa/", lista_tarefa, name = "tarefas"),
    path("sobre/", pagina_sobre, name = "sobre"),
    path("cadastros/", cadastros, name = "cadastros"),
]
staticfiles_urlpatterns = staticfiles_urlpatterns()