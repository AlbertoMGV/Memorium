"""MemoriumAPI URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from api.resources import *
from api import views

user_resource = userResource()
atencion_resource = atencionResource()
funciones_resource = funcionesResource()
lenguaje_resource = lenguajeResource()
memoria_resource = memoriaResource()
percepcion_resource = percepcionResource()
lectoescritura_resource = lectoescrituraResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login', views.login, name='login'),
	url(r'^register', views.register, name='register'),
	url(r'^saveAtencion', views.saveAtencion, name='saveAtencion'),
	url(r'^saveFunciones', views.saveFunciones, name='saveFunciones'),
	url(r'^saveLenguaje', views.saveLenguaje, name='saveLenguaje'),
	url(r'^saveMemoria', views.saveMemoria, name='saveMemoria'),
	url(r'^savePercepcion', views.savePercepcion, name='savePercepcion'),
	url(r'^saveLectoescritura', views.saveLectoescritura, name='saveLectoescritura'),
	url(r'^getAtencion', views.getAtencion, name='getAtencion'),
]
