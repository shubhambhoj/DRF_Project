from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

# Search Filter  in REST API
'''
from rest_framework import filters
from rest_framework.generics import ListAPIView

class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'roll','city']
'''
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[IsAdminUser]
    #permission_classes=[AllowAny]
    #permission_classes=[IsAuthenticatedOrReadOnly]
    #permission_classes=[DjangoModelPermissions]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    permission_classes=[DjangoObjectPermissions]


