from django.db import models


class Pirate(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name
