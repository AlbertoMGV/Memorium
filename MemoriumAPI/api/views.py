from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.status import (HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_200_OK)
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.models import *
from django.core import serializers
from api.serializers import * 
import json

# Create your views here.

@api_view(["POST"])
def login(request):
	if request.method == 'POST':
		# emma_id getting by token
		em = request.data.get('email')
		try:
			usr = user.objects.all().get(email=em)
			if usr.contra == request.data.get('contra'):
				return Response({'result': 'true'}, status=HTTP_200_OK)
			else: 
				return Response({'result': 'false'}, status=HTTP_401_UNAUTHORIZED)
		except:
			return Response({'result': 'false'}, status=HTTP_401_UNAUTHORIZED)
            

@api_view(["POST"])
def register(request):
	if request.method == 'POST':
		em = request.data.get('email')
		try:
			tst = user.objects.all().get(email=em)
			return Response({'result': 'false'}, status=HTTP_401_UNAUTHORIZED)
		except:
			usr = user()
			usr.email = request.data.get('email')
			usr.nombre = request.data.get('nombre')
			usr.contra = request.data.get('contra')
			usr.save()
			return Response({'result': 'true'}, status=HTTP_200_OK)


@api_view(["POST"])
def saveAtencion(request):
    if request.method == 'POST':
        # emma_id getting by token
        resul = atencion()
        resul.user_id = request.data.get('user_id')
        resul.puntuacion = request.data.get('puntuacion')
        resul.save()
        return Response({'result': 'true'}, status=HTTP_200_OK)

@api_view(["POST"])
def saveFunciones(request):
    if request.method == 'POST':
        # emma_id getting by token
        resul = funciones()
        resul.user_id = request.data.get('user_id')
        resul.puntuacion = request.data.get('puntuacion')
        resul.save()
        return Response({'result': 'true'}, status=HTTP_200_OK)
        
@api_view(["POST"])
def saveLenguaje(request):
    if request.method == 'POST':
        # emma_id getting by token
        resul = lenguaje()
        resul.user_id = request.data.get('user_id')
        resul.puntuacion = request.data.get('puntuacion')
        resul.save()
        return Response({'result': 'true'}, status=HTTP_200_OK)

@api_view(["POST"])
def saveMemoria(request):
    if request.method == 'POST':
        # emma_id getting by token
        resul = memoria()
        resul.user_id = request.data.get('user_id')
        resul.puntuacion = request.data.get('puntuacion')
        resul.save()
        return Response({'result': 'true'}, status=HTTP_200_OK)

@api_view(["POST"])
def savePercepcion(request):
    if request.method == 'POST':
        # emma_id getting by token
        resul = percepcion()
        resul.user_id = request.data.get('user_id')
        resul.puntuacion = request.data.get('puntuacion')
        resul.save()
        return Response({'result': 'true'}, status=HTTP_200_OK)
        
@api_view(["POST"])
def saveLectoescritura(request):
    if request.method == 'POST':
        # emma_id getting by token
        resul = lectoescritura()
        resul.user_id = request.data.get('user_id')
        resul.puntuacion = request.data.get('puntuacion')
        resul.save()
        return Response({'result': 'true'}, status=HTTP_200_OK)

@api_view(["POST"])
def getAtencion(request):
	if request.method == 'POST':
		# emma_id getting by token
		uid = request.data.get('user_id')
		try:
			res = atencion.objects.filter(user_id=uid)
			res_ser = atencionSerializer(res, many=True)
			aaa = json.loads(res_ser.data)
			return Response({"a":"s"}, status=HTTP_200_OK)
		except:
			return Response({'result': 'false'}, status=HTTP_401_UNAUTHORIZED)