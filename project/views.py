# -*- coding: utf-8 -*-
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from people.models import Person


class HomeView(generic.edit.FormView):

    template_name = 'home.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        self.object = form.save()
        person, success = Person.objects.get_or_create(user=self.object)
        person.slug = slugify(self.request.POST['username'])
        person.save()

        #messages.info(request, "Thanks for registering. You are now logged in.")
        self.object = authenticate(username=self.request.POST['username'],
                                   password=self.request.POST['password1'])
        login(self.request, self.object)
        return HttpResponseRedirect("/profile/{0}".format(person.slug))