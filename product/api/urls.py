from django.urls import include, path
from django.contrib import admin

app_name = 'api'

urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('api/v1/admin/', admin.site.urls)
]
