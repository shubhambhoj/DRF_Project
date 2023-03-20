from django.contrib import admin
from django.urls import path,include
from api.views import StudentModelView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studentapi', StudentModelView,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
