from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from rest_framework.decorators import api_view
from apps.users.models import User


@api_view(["GET", "POST"])
#  GET / INSERT USUARIO
def user_api_view(request):

    if request.method == "GET":
        users = User.objects.all()
        # con el many = True se nos permite traer mas de un registro
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        # me permite la opcion de hacer pruebas insertando usuarios desde el entorno de django
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
#  GET , UPDATE y DELETE USUARIO BY ID
def user_detail_api_view(request,pk):
    # querySet (variables con las que realizo querys a la BD)
    user = User.objects.filter(id = pk).first()

    if user:
        if request.method == "GET":
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        elif request.method == "PUT":
            user_serializer = UserSerializer(user,data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'}, status = status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    

        
