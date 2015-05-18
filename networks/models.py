# -*- coding: utf-8 -*-
from django.db import models




class BaseNetwork(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Network(BaseNetwork):
    pass


class Chapter(BaseNetwork):
    network = models.ForeignKey(Network, null=True, blank=True)
