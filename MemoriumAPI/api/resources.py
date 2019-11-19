from tastypie.resources import ModelResource
from api.models import *
from tastypie.authorization import Authorization

class userResource(ModelResource):
    class Meta:
        queryset = user.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        fields = ['id','email', 'nombre']

class atencionResource(ModelResource):
    class Meta:
        queryset = atencion.objects.all()
        resource_name = 'atencion'
        authorization = Authorization()

class funcionesResource(ModelResource):
    class Meta:
        queryset = funciones.objects.all()
        resource_name = 'funciones'
        authorization = Authorization()

class lenguajeResource(ModelResource):
    class Meta:
        queryset = lenguaje.objects.all()
        resource_name = 'lenguaje'
        authorization = Authorization()

class memoriaResource(ModelResource):
    class Meta:
        queryset = memoria.objects.all()
        resource_name = 'memoria'
        authorization = Authorization()

class percepcionResource(ModelResource):
    class Meta:
        queryset = percepcion.objects.all()
        resource_name = 'percepcion'
        authorization = Authorization()

class lectoescrituraResource(ModelResource):
    class Meta:
        queryset = lectoescritura.objects.all()
        resource_name = 'lectoescritura'
        authorization = Authorization()