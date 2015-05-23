# -*- coding: utf-8 -*-
from django.views import generic
from .models import Event

class QuerySetMixin(object):

    model = Event


class DetailView(QuerySetMixin, generic.DetailView):

    pass


# class ListView(QuerySetMixin, generic.ListView):

#     pass