from django.shortcuts import render
from .models import Song,Singer
from .serializers import SongSerializer,SingerSerializer
from rest_framework.viewsets import ModelViewSet


class SingerView(ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
    
class SongView(ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
