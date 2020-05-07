"""cricket_planet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^$', serve, kwargs={'path':'index.html'}),
    url(r'^(?!/?static/) (?!/?path/) (?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s',permanent=False)),
    
    path('admin/', admin.site.urls),
    path('teams/', include('cricket_teams.urls')),
    path('match/', include('matches.urls')),
    # path('player/', include('players.urls')),
    # path('score/', include('score_points.urls')),
]
