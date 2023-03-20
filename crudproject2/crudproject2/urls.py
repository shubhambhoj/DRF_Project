from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.add_show, name='home'),
    path('', views.AddShow.as_view(), name='home'),
    #path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('delete/<int:id>/', views.DeleteData.as_view(), name='deletedata'),
    #path('<int:id>/', views.update_data, name='updatedata'),
    path('<int:id>/', views.UpdateData.as_view(), name='updatedata'),
    path('api/',include('enroll.api.urls')),
   
]