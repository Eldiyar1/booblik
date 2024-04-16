from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from core.settings.swagger import swagger_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.geolocation.urls")),
    path("api/v1/", include("apps.vacancy.urls")),
    path("api/v1/", include("apps.feedback.urls")),
    path("api/v1/", include("apps.event.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
] + swagger_urlpatterns


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
