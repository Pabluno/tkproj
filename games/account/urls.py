from django.conf.urls import patterns, include, url

from .views import SignUpView

urlpatterns = patterns('account.views',
	url(r'^home$', 'home', name='account_home'),
	url(r'signup$', SignUpView.as_view(), name='account_signup'),
)


