from django.conf.urls import patterns, url
from current import views

urlpatterns = patterns('',

	url(r'^$', views.index, name = 'index'),
	url(r'^about/$', views.about, name = 'about' ),
	url(r'^projects/$', views.projects, name = 'projects'),
	url(r'^interests/$', views.interests, name = 'interests'),
	url(r'^poli/$', views.poli, name = 'poli'),
	url(r'^comp/$', views.comp, name = 'comp'),
	url(r'^contact/$', views.contact, name = 'contact'),

	)