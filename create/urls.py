from django.urls import path 
from . import views

urlpatterns = [
    path('', views.create_new, name='create_new'),
    path('download/<int:pk>/', views.download, name='download'),
]