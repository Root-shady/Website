from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'about/', views.about, name='about'), # This is the bloig about me section
        )
