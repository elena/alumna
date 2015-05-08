from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'project.views.home', name='home'),
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    url('^auth/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
]
