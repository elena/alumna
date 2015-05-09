from django.db import models
from networks.models import Chapter


class Event(models.Model):
    chapter = models.ForeignKey(Chapter)
    name = models.CharField(max_length=128)
    date = models.DateField()
    desc = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
