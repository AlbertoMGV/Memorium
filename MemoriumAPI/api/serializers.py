from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import *


class atencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = atencion
        fields = ('id', 'puntuacion', 'fecha', 'user_id')
