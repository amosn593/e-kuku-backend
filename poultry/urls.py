
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include('main_app.urls')),
    path('api/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')), 
    path('admin/', admin.site.urls),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
