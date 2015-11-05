from django.conf.urls import patterns, url
from vpn import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/', views.register, name='register'),
        url(r'^logout/', views.logout, name='logout'),
    )
