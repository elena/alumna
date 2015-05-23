from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    # Alumna
    url(r'^profile/', include('people.urls')),

    # # Events
    # url(r'^event/', include('events.urls')),

    # Networks
    url(r'^networks/', include('networks.urls')),

    #url('^social/', include('social.apps.django_app.urls', namespace='social')),
    url('^auth/', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^admin/', include(admin.site.urls)),
]
