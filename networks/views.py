# -*- coding: utf-8 -*-
from django.views import generic
from .models import Network


class QuerySetMixin(object):

    model = Network


class ListView(QuerySetMixin, generic.ListView):

    pass


# class DetailView(QuerySetMixin, generic.DetailView):

#     pass

## @@ TODO:  Add django-braces: LoginRequiredMixin
