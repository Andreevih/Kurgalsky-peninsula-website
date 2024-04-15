from django.contrib import admin
from django.urls import path, include

# Это файл для отслеживания URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
