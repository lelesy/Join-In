# coding: utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from Join.core import views as core_views
from Join.authentication import views as join_auth_views
from Join.activities import views as activities_views
from Join.search import views as search_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', join_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture, name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture, name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^feeds/', include('Join.feeds.urls')),
    url(r'^questions/', include('Join.questions.urls')),
    url(r'^articles/', include('Join.articles.urls')),
    url(r'^messages/', include('Join.messenger.urls')),
    url(r'^notifications/$', activities_views.notifications, name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications, name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications, name='check_notifications'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
