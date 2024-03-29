from django.conf.urls import patterns, include, url
import RandomPages.views as vista

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home$',vista.home, name='home'),
    url(r'^test/(.+)/$', vista.quiz_guess, name='quiz_guess'),
    url(r'^search/(.+)/$', vista.devuelve_tweets, name='devuelve_tweets'),
    url(r'^add/(.+)/$', vista.agregado, name='agregado'),
    url(r'^discover/(.+)/$', vista.discover),
    url(r'^like/(.+)/$', vista.like),
    url(r'^dislike/(.+)/$', vista.dislike),
    url(r'^$', vista.cover),
    # url(r'^$', 'RandomPages.views.home', name='home'),
    # url(r'^RandomPages/', include('RandomPages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
