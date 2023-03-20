from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    serializer_class=StudentSerializer

    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)
