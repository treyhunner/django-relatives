from django.db import models


class Pirate(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class Pet(models.Model):
    owner = models.ForeignKey(Pirate)


class Ship(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Sailor(models.Model):
    name = models.CharField(max_length=80)
    ship = models.ForeignKey(Ship, null=True)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=80)
    movies = models.ManyToManyField('Movie', related_name='actors')


class Movie(models.Model):
    name = models.CharField(max_length=80)


class Something(models.Model):
    text = models.CharField(max_length=10)


class NotInAdmin(models.Model):
    fk = models.ForeignKey(Something)
