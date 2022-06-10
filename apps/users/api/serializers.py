from dataclasses import field, fields
from unittest.util import _MAX_LENGTH
from click import password_option
from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
# Tranforman Modelos o Entidades a un formato JSON

# Serializador en base a un modelo
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Escogo los campos de la tabla con los que deseo trabajar en los api_views
        fields = '__all__'
        
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','imagePfp']
        
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# Similar a DTOS de Spring en los que en vez de realizar peticiones directamente manipulando la entidad
# o modelo creas una clase intermedia por seguridad en el manejo de los datos y flexibilidad en cuanto 
# los tipos de datos asignados

# class TestUserSerializer(serializers.Serializer):
#     id = serializers.CharField(max_lengh = 255)
#     # Puedo crear métodos para crear validaciones de los datos asignados
#     def validate__attr(self,value):
        # if (ocurre error):
            # raise serializers.ValidationError('Mensaje de error que eliga')
        # return value
