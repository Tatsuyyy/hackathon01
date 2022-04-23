from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView ,SpectacularSwaggerView

urlpatterns = [
    # TODO: そのうち削除
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(), name='swagger_ui'),
    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('sample_api/', include('sample_api.urls')),
]

if settings.DEBUG:  
    urlpatterns += [
        path('schema', SpectacularAPIView.as_view(), name='schema'),
        path('', SpectacularSwaggerView.as_view(), name='swagger_ui'),
    ]