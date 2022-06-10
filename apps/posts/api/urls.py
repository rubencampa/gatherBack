from django.urls import path
from apps.posts.api.api import post_api_view , post_detail_api_view ,tema_api_view,getUsuarioByTitulo

urlpatterns = [
    path('temas/',tema_api_view, name='tema_api_view'),
    path('posts/',post_api_view, name='post_api_view'),
    path('posts/<int:pk>/',post_detail_api_view, name='post_detail_api_view'),
    path('posts/search/<str:pk>/',getUsuarioByTitulo, name='getUsuarioByTitulo'),
]