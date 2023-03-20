from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

from rest_framework.routers import DefaultRouter
from api.views import StudentModelView

router=DefaultRouter()
router.register('studentapi', StudentModelView, basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view(), name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(), name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(), name='varifytoken'),
]
