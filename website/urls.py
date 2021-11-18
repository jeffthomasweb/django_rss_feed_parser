from django.contrib import admin
from django.urls import include, path

#For better security change the admin/ URL to something less known to avoid bots that scan websites for vulnerabilities
urlpatterns = [
    path('', include('mysite.urls')),
    path('admin/', admin.site.urls),
]
