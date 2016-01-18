from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^$','main.views.home', name='games_home')
)

urlpatterns += patterns(
	'django.contrib.auth.views',

	url(r'^login/$', 'login',
	    {'template_name': 'login.html'},
	    name='games_login'),

	url(r'^logout/$', 'logout',
	    {'next_page': 'games_home'},
	    name='games_logout'),
)


