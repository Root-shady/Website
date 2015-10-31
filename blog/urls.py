from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'about/', views.about, name='about'), # This is the bloig about me section
        url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<post_title>[\w\-]+)/$', views.single_post, name='single_post'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        )
