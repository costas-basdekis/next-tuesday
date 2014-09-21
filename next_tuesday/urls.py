from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views import generic

from . import views

urlpatterns = patterns('',
    url(r'^$', views.NextTuesdayView.as_view(), name='home'),
    url(r'^(?P<word>\w+)/?$', views.NextTuesdayView.as_view(), name='home-word'),
    url(r'^.*$', generic.RedirectView.as_view(url='/'), name='home-rest'),

    #url(r'^admin/', include(admin.site.urls)),
)
