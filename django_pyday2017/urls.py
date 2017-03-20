"""django_pyday2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, static
from django.conf import settings as st
from django.contrib import admin

# README: TOCAR!!
# Incluir la url de acceso a las aplicaciones
urlpatterns = [
    url(r'', include('events.urls')),
    url(r'^admin/', admin.site.urls),
] + static.static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)
