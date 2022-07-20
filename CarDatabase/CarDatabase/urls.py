"""CarDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Auth.urls')),
    path('', include('CarData.urls')),
    path('custom-admin-auth/', include('AdminAuth.urls')),
    path('admin-sites/', include('AdminSite.urls')),
    path('user/', include('CustomUser.urls')),
]


# Because django is not a dedicated file serving service,
# in production this does not work but in this case (DEBUG) we can use for serving files.
# Because the lack of time I cannot set up a dedicated server (like ngix) which
# could serve media files so now we are gonna serve these from a server url.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)