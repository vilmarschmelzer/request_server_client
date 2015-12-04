"""request_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from requestapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^category/$', CategorySaveView.as_view(), name='category-save'),
    url(r'^category/(?P<category_id>\d+)/$', CategorySaveView.as_view(), name='category-save'),
    url(r'^category-list/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category-list-rest/$', CategoryListRestView.as_view(), name='category-list-rest'),

    url(r'^item/$', ItemSaveView.as_view(), name='item-save'),
    url(r'^item/(?P<item_id>\d+)/$', ItemSaveView.as_view(), name='item-save'),
    url(r'^item-list/$', ItemListView.as_view(), name='item-list'),

    #url(r'^test-angular/$', TestAngularView.as_view(), name='test-angular'),

]
