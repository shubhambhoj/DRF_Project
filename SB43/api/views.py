from api.models import Song,Singer
from api.serializers import SongSerializer,SingerSerializer
from rest_framework.viewsets import ModelViewSet


class SongView(ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer

class SingerView(ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
   
