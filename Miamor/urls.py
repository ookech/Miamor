
from django.contrib import admin
from django.urls import path,include
from miamorapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miamorapp.urls')),
]
