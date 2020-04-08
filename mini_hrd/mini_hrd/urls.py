"""mini_hrd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from karyawan.views import karyawan_all,karyawan_insert, karyawan_detail, edit, karyawan_delete, karyawan_update

urlpatterns = [
    url(r'^$', karyawan_all, name='karyawan_all'),
    url(r'^add',karyawan_insert, name='karyawan_insert'),
    url(r'^detail/(?P<pk>\d+)/$',karyawan_detail, name='karyawan_detail'),
    url(r'^update/(?P<pk>\d+)/$',karyawan_update, name='karyawan_update'),
    url(r'^delete/(?P<pk>\d+)/$',karyawan_delete, name='karyawan_delete'),
    
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit'),
    url(r'^admin/', admin.site.urls),
]
