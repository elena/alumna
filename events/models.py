from django.db import models


class BaseEvent(models.Model):

    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    code = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.name


class Event(BaseEvent):
    """ Official event.
    """
    chapter = models.ForeignKey('networks.Chapter')

    def __str__(self):
        if self.name:
            return self.name
        else:
            date = self.date_start.strftime("%B %Y")
            return "{0} {1}".format(self.chapter.chapter_name, date)


class EventRole(models.Model):
    event = models.ForeignKey(Event)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=32)
    role = models.ForeignKey('events')

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


# ---
# Definitions only

class Role(models.Model):
    """ The role of organiser is special.

    Other roles may require special permissions in future.
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
