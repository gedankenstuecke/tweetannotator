"""twitter_annotator URL Configuration

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
from main.views import index, annotate, graph, about, download_annotations, analysis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('annotate/<int:tweet_id>/<str:answer>/', annotate, name='annotate'),
    path("graph", graph, name='graph'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('download-annotations/', download_annotations, name='download_annotations'),
    path('analysis/', analysis, name='analysis'),
]
