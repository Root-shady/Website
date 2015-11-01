from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
import blog, home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'grappelli/', include('grappelli.urls')),
    url(r'^$', 'home.views.home', name="home"),  # The website homepage
    url(r'^home/', include('home.urls')), # The website homepage
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Any pattern states that for any file requested with a URL starting with media/, the request will be passed to the django.views.static view.
# This views handles the dispatching of upload media files for you.
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
