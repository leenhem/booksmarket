"""stud1 URL Configuration

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
# from websocket import views


from . import views

urlpatterns = [
    # url(r'^index/\d{2}/$', views.index),#正则匹配数字
    url(r'^index/(?P<id>[0-9]{2})/$', views.index),#正则匹配 向后台传递数据
    url(r'^insert/(?P<name>[a-z]{4})/$', views.insert),#插入数据
    url(r'^insert2/(?P<name>[a-z]{4})/$', views.insert2),#插入数据
    url(r'^index/$', views.index),
    url(r'^select/$', views.select),#查询数据
    url(r'^select2/(?P<name>[a-z]{4})/$', views.select2),#查询数据
    url(r'^select0/(?P<name>[a-z]{6})/$', views.select0),#查询数据
    url(r'^select2/(?P<name>[a-z]{4}_[a-z]{4})/$', views.select2),#查询数据
    url(r'^createauthor/(?P<name>[a-z]{4})/$', views.createauthor),#查询数据
    url(r'^selectauthorall/$', views.selectauthorall),#查询数据
    url(r'^addbook/(?P<name>[a-z]{6})/(?P<author>[a-z]{4})/$', views.addbook),#查询数据
    # url(r'^echo_once', views.echo_once),
]
