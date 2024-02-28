from django.contrib import admin
from django.urls import path,include
from app1.views import *

urlpatterns = [
    path('', include('app1.urls')),
    path('admin/', admin.site.urls),
]
