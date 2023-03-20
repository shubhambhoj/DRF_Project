from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class StudentListAPIView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='show_info'

class StudentRetrieveAPIView(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='show_info'
    
class StudentCreateAPIView(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='change_info'
    
class StudentUpdateAPIView(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='change_info'

class StudentDestroyAPIView(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='change_info'
