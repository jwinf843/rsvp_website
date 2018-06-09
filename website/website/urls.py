"""website URL Configuration

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
from django.contrib import admin
from django.urls import path
from rsvp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('guests/', views.guests),
    path('guests_jp/', views.guests_jp),
    path('nav/', views.nav),
    path('nav_jp/', views.nav_jp),
    path('jp/', views.jp),
    path('process/', views.process),
    # Always leave the index url at the bottom
    path('', views.index),
]

