from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^$', CreateView.as_view(template_name='home.html',
                                 form_class=UserCreationForm, success_url='/'), name='home'),
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    url('^auth/', include('django.contrib.auth.urls', namespace='auth')),

    # Alumna
    url(r'^alumna/', include('people.urls')),

    # Events
    url(r'^event/', include('events.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
