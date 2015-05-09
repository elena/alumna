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
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username

    def save(self, *args, **kwargs):
        super(Person, self).save()
        event = Event.objects.get(pk=1)
        role = Role.objects.get(pk=3)
        PersonRole.objects.get_or_create(person=self, event=event, role=role)


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
