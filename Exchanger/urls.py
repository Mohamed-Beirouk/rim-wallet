from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Agency.urls', namespace='Agency')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
