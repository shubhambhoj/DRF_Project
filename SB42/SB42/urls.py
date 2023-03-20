
from django.contrib import admin
from django.urls import path,include
from api.views import StudentView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studentapi', StudentView,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]
