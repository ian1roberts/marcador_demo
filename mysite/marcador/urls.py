from django.conf.urls import patterns, include, url


urlpatterns = patterns('marcador.views',
    url(r'^user/(?P<username>[-\w]+)/$', 'bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^create/$', 'bookmark_create', name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'bookmark_edit', name='marcador_bookmark_edit'),
    url(r'^$', 'bookmark_list', name='marcador_bookmark_list'),
)
