"""MemoriumAPI URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from api.resources import *

user_resource = userResource()
atencion_resource = atencionResource()
funciones_resource = funcionesResource()
lenguaje_resource = lenguajeResource()
memoria_resource = memoriaResource()
percepcion_resource = percepcionResource()
lectoescritura_resource = lectoescrituraResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(user_resource.urls)),
    url(r'^api/', include(atencion_resource.urls)),
    url(r'^api/', include(funciones_resource.urls)),
    url(r'^api/', include(lenguaje_resource.urls)),
    url(r'^api/', include(memoria_resource.urls)),
    url(r'^api/', include(percepcion_resource.urls)),
    url(r'^api/', include(lectoescritura_resource.urls))
]
