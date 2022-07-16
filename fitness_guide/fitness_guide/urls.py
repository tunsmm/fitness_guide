"""fitness_guide URL Configuration

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
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path
import debug_toolbar


handler404 = "menu.views.page_not_found"  # noqa
handler500 = "menu.views.server_error"  # noqa

urlpatterns = [
    path("", include("menu.urls")),  # main page
    path('admin/', admin.site.urls),  # admin section
    path("auth/", include("users.urls")),  # registration and autorization
    path("auth/", include("django.contrib.auth.urls")),  # if in users.urls don't exist this template
    path('about/', include('django.contrib.flatpages.urls')),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
