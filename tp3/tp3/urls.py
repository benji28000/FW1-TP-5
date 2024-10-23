from django.contrib import admin
from django.urls import path, include

urlpatterns = [path('admin/', admin.site.urls, name='admin'),
path('bonnes_lectures/', include('bonnes_lectures.urls'),name='bonnes_lectures'),
]