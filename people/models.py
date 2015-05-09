from django.contrib.auth.models import User
from django.db import models
from events.models import Event


class Role(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username


class PersonRole(models.Model):
    person  = models.ForeignKey(Person)
    event  = models.ForeignKey(Event)
    role  = models.ForeignKey(Role)


class PersonSkill(models.Model):
    person  = models.ForeignKey(Person)
    skill  = models.ForeignKey(Skill)


class PersonEvent(models.Model):
    person  = models.ForeignKey(Person)
    event  = models.ForeignKey(Event)
