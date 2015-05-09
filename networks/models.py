from django.db import models


class Network(models.Model):
   name = models.CharField(max_length=128)
   url = models.URLField(null=True, blank=True)

   def __str__(self):
       return self.name


class Chapter(models.Model):
   network = models.ForeignKey(Network, null=True, blank=True)
   name = models.CharField(max_length=128)
   url = models.URLField(null=True, blank=True)

   def __str__(self):
       return self.name
