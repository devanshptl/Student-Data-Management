from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('info/', views.info, name = "info"),
    path('delete/<id>/',views.delete, name = "delete"),
    path('update/<id>/',views.update, name = "update"),
    
]