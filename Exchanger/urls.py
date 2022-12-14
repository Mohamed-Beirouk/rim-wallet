from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Agency.urls', namespace='Agency')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

    
    #documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    #test
]