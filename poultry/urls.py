
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = 'E-KUKU admin'
admin.site.site_title = 'E-KUKU admin'
admin.site.index_title = 'E-KUKU administration'

if settings.DEBUG == True:
    urlpatterns = [
        path('main/', include('main_app.urls')),
        # path('mpesa/', include('mpesa.urls')),
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path('main/', include('main_app.urls')),
        # path('mpesa/', include('mpesa.urls')),
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('admin/', admin.site.urls),
    ]
