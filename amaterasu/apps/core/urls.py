from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from views import IndexView, RedirectToIndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'}, name="auth_login"),
    url(r'^logout/$', RedirectToIndexView.as_view(), name="auth_logout"),
    url(r'^admin/', include(admin.site.urls)),
)