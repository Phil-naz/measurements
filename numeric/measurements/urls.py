from django.urls import path, include
from .views import *




urlpatterns = [
    path('', measurements, name='measurements'),
    path('', measurements, name='home'),
    path('meas_add', meas_add, name='meas_add'),
    path('comparison/<str:comp_pk>/', comparison, name='comparison'),
]