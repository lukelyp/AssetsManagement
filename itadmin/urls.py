"""itadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
admin.autodiscover()
from django.contrib.auth import views as auth_views
from app import views

import debug_toolbar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^host_list/$', views.host_list, name="host_list"),
    url(r'^host_add/$', views.host_edit, name="host_add"),
    url(r'^host_edit/(?P<id>\d+)/$', views.host_edit, name="host_eidit"),
    url(r'^host_delete/$', views.host_edit, name="host_delete"),
    url(r'^exec_command/$', views.exec_command, name="exec_command"),
]
