
from django.contrib import admin
from django.urls import path,include
from api import views

# from api.views import student_api
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('studentapi', student_api,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include(router.urls)),
    path('studentapi/',views.student_api),
    path('studentapi/<int:pk>/',views.student_api),
    path('auth/',include('rest_framework.urls')),
]   
