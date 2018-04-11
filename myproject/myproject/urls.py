from django.conf.urls import patterns, include, url
from django.contrib import admin
from cmsUsersPut import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio, name="Página inicio"),
    url(r'(.+)', views.pagina, name="Página"),
)
