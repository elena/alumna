# -*- coding: utf-8 -*-
from django.db import models


class BaseNetwork(models.Model):
    url = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to="networks/logos", null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Network(BaseNetwork):
    name = models.CharField(max_length=128)


class Chapter(BaseNetwork):
    network = models.ForeignKey(Network, null=True, blank=True)
    locale = models.CharField(max_length=128)
    name = models.CharField(max_length=128, null=True, blank=True,
                            help_text="If different from '{network} {locale}'.")

    def _get_chapter_name(self):
        if self.name:
            return self.name
        else:
            return "{0} {1}".format(self.network.name, self.locale)
    chapter_name = property(_get_chapter_name)

    def __str__(self):
        return self.chapter_name
