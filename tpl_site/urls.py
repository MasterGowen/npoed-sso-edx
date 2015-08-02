from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.decorators.csrf import csrf_exempt

from apps.core.views import AccessTokenDetailView
from apps.core.decorators import set_auth_cookie, external_redirect
from apps.profiler.views import CustomActivationView


urlpatterns = patterns(
    '', url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.core.urls')),
    url(r'^', include('apps.profiler.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^accounts/activate/(?P<activation_key>\w+)/$',
        CustomActivationView.as_view(), name='registration_activate'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^accounts/reset/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
    url('^accounts/password_change/',
        'django.contrib.auth.views.password_change',
        name="password_change"),
    url(r'^accounts/password_changed/$',
        'django.contrib.auth.views.password_change_done',
        name="password_change_done"),
    

    url(r'^login/', set_auth_cookie(login), name='login'),
    url(r'^logout/', external_redirect(set_auth_cookie(logout)),
        {'next_page': '/'}, name='logout'),

    url('^oauth2/access_token/(?P<token>[\w]+)/$',
        csrf_exempt(AccessTokenDetailView.as_view()),
        name='access_token_detail'),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace = 'oauth2')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT, }),
        )
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
