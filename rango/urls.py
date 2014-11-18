from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^pages/(?P<page_id>\d+)/$',
                           views.detail, name='detail'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^categories/([a-z0-9-]+)/$',
                           views.category, name='category'),
                       url(r'^categories/$', views.list_categories,
                           name='categories'),
                       url(r'^pages/$', views.list_pages, name='pages'),
                       url(r'^like/(?P<category_id>\d+)/$',
                           views.like, name='like'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^signin/$', views.signin, name='signin'),
                       url(r'^restricted/', views.restricted,
                           name='restricted'),
                       url(r'^signout/$', views.signout, name='signout'),
                       url(r'^newpage/$', views.add_page, name='addpage'),
                       url(r'^newcategory/$', views.add_category,
                           name='newcategory'),
                       url(r'^jquery/$', views.jq, name='jq'), )
