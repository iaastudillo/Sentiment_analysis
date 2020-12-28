from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('probar_modelo/', views.probar_modelo),
    path('alimentar_modelo/', views.alimentar_modelo),
    path('entrenar_modelo/', views.entrenar_modelo)
]
