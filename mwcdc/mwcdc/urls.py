from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from places.views import PlaceViewSet
from skyline.views import ViewpointViewSet

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mwcdc.views.home', name='home'),
    # url(r'^mwcdc/', include('mwcdc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

router = routers.SimpleRouter()
router.register(r'places', PlaceViewSet)
router.register(r'viewpoints', ViewpointViewSet)
urlpatterns += router.urls
