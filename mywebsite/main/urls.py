from django.urls import path
from . import views
# Это файл для отслеживания URL

urlpatterns = [
    path('', views.index),
    path('history', views.history),
    path('excursus', views.excursus),
    path('nature', views.nature),
]
