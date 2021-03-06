"""Inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]'''

#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from store_app.forms import LoginForm

from django.conf.urls import include, url


#from django.conf.urls import url, include
#from django.contrib import admin
#from django.contrib.auth import views as auth_views

#from store_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/',admin.site.urls),
    url(r'', include('store_app.urls')),#^myapp/
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)