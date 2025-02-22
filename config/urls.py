from django.contrib import admin
from django.urls import path, include, re_path
from app import urls
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('api-auth/', include('rest_framework.urls')),
]
