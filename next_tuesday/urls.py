from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.NextTuesday.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
