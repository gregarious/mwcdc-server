from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from places.views import PlaceViewSet, SearchPlaces
from skyline.views import ViewpointViewSet

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

router = routers.SimpleRouter()
router.register(r'^api/places', PlaceViewSet)
router.register(r'^api/viewpoints', ViewpointViewSet)
urlpatterns += router.urls

urlpatterns += patterns('',
    url(r'^search/$', SearchPlaces.as_view()),
)
