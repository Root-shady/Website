from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('', 
        url(r'^$', views.home, name='home'),
        url(r'about/', views.about, name='about'), # this is a description about my whole website
        )
