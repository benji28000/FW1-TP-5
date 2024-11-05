from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('admin/', admin.site.urls, name='admin'),
path('bonnes_lectures/', include('bonnes_lectures.urls'),name='bonnes_lectures'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
