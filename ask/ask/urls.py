"""ask URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

import qa

#from ask.views import found, not_found, init25
#from qa.views import index, popular, ask, login_view, signup

urlpatterns = [

#    url(r'^$', index),

url(r'^login/', admin.site.urls),
url(r'^signup/', admin.site.urls),
url(r'^ask/', admin.site.urls),
url(r'^popular/', admin.site.urls),
url(r'^new/', admin.site.urls),



    url(r'^admin/', admin.site.urls),
    url(r'^question/', include('qa.urls')),
    url(r'^/', admin.site.urls),
]
