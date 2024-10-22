from django.contrib import admin
from django.urls import path, include

urlpatterns = [path('admin/', admin.site.urls),
path('bonnes_lectures/', include('bonnes_lectures.urls')),
]