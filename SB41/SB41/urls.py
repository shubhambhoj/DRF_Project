
from django.contrib import admin
from django.urls import path,include
from api.views import SongView,SingerView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('song', SongView,basename='song')
router.register('singer', SingerView, basename='singer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
