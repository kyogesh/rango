from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/([a-z0-9-]+)/$', views.category, name='category'),
    url(r'^like/(?P<category_id>\d+)/$', views.like, name='like'),
)
