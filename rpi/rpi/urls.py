from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('monitor.views',
    (r'^$', 'index'),
    (r'^index/$', 'index'),
    (r'^index/(?P<chart>\d)/$', 'index'),

    # Examples:
    # url(r'^$', 'rpi.views.home', name='home'),
    # url(r'^rpi/', include('rpi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
