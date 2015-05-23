from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    profile = models.ImageField(upload_to="people/profile", null=True, blank=True)
    desc_social = models.TextField(null=True, blank=True)
    desc_skill = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username


class PersonEventRole(models.Model):
    person = models.ForeignKey('people.Person')
    event = models.ForeignKey('events.Event')
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return "{0} -- {1}".format(self.event.name, self.name)


# class PersonSkill(models.Model):
#     person  = models.ForeignKey(Person)
#     skill  = models.ForeignKey(Skill)


# class PersonEvent(models.Model):
#     person  = models.ForeignKey(Person)
#     event  = models.ForeignKey(Event)
