from rest_framework import status,serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.posts.api.serializers import PostSerializer,TemaSerializer,GetPostSerializer
from rest_framework.decorators import api_view
from apps.posts.models import Post,Tema

@api_view(["GET", "POST"])
#  GET / INSERT TEMA
def tema_api_view(request):

    if request.method == "GET":
        temas = Tema.objects.all()
        # con el many = True se nos permite traer mas de un registro
        temas_serializer = TemaSerializer(temas, many=True)
        return Response(temas_serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        # me permite la opcion de hacer pruebas insertando usuarios desde el entorno de django
        temas_serializer = TemaSerializer(data=request.data)
        if temas_serializer.is_valid():
            temas_serializer.save()
            return Response(temas_serializer.data, status = status.HTTP_201_CREATED)
        return Response(temas_serializer.errors)

@api_view(["GET", "POST"])
#  GET / INSERT POST
def post_api_view(request):

    if request.method == "GET":
        posts = Post.objects.all()
        # con el many = True se nos permite traer mas de un registro
        posts_serializer = GetPostSerializer(posts, many=True)
        return Response(posts_serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        # me permite la opcion de hacer pruebas insertando usuarios desde el entorno de django
        posts_serializer = PostSerializer(data=request.data)
        
        if posts_serializer.initial_data['tipoPost'] == 2:
            posts_serializer.initial_data['contenido'] = serializers.CharField(required=False)

        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status = status.HTTP_201_CREATED)
        return Response(posts_serializer.errors)

@api_view(['GET','PUT','DELETE'])
#  GET , UPDATE y DELETE USUARIO BY TEMA
def post_detail_api_view(request,pk):
    # querySet (variables con las que realizo querys a la BD)
    posts = Post.objects.filter(tema = pk)
    # posts = Post.objects.values_list('tema')
    if posts:
        if request.method == "GET":
            posts_serializer = GetPostSerializer(posts, many=True)
            return Response(posts_serializer.data, status = status.HTTP_200_OK)
        elif request.method == "PUT":
            posts_serializer = PostSerializer(posts,data = request.data)
            if posts_serializer.is_valid():
                posts_serializer.save()
                return Response(posts_serializer.data, status = status.HTTP_200_OK)
            return Response(posts_serializer.errors, status = status.HTTP_204_BAD_REQUEST)
        elif request.method == "DELETE":
            posts.delete()
            return Response({'message':'Publicación eliminado correctamente'}, status = status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
#  GET USUARIO BY Titulo
def getUsuarioByTitulo(request,pk):
    # querySet (variables con las que realizo querys a la BD)
    posts = Post.objects.filter(titulo = pk)
    # posts = Post.objects.values_list('tema')
    if posts:
        if request.method == "GET":
            posts_serializer = GetPostSerializer(posts, many=True)
            return Response(posts_serializer.data, status = status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado un posts con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
