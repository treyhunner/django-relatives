from django.db import models


class Pirate(models.Model):

    """Pirates have no admin URL"""

    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class Pet(models.Model):

    """Pet have an admin URL and link to Pirates"""

    owner = models.ForeignKey(Pirate)


class Ship(models.Model):

    """Ships have an admin URL and are linked to by sailors"""

    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Sailor(models.Model):

    """Sailors have an admin URL and sometimes link to ships"""

    name = models.CharField(max_length=80)
    ship = models.ForeignKey(Ship, null=True)

    def __unicode__(self):
        return self.name


class Actor(models.Model):

    """Actors have an admin URL and a many-to-many relationship with movies"""

    name = models.CharField(max_length=80)
    movies = models.ManyToManyField('Movie', related_name='actors')


class Movie(models.Model):

    """Movies have an admin URL and are linked to (m2m) by actors"""

    name = models.CharField(max_length=80)


class Something(models.Model):

    """Somethings don't have an admin URL and are linked to by NotInAdmins"""

    text = models.CharField(max_length=10)


class NotInAdmin(models.Model):

    """NotInAdmins do not have an admin URL and link to Somethings"""

    fk = models.ForeignKey(Something)
