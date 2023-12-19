from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Pirate(models.Model):

    """Pirates have no admin URL"""

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Pet(models.Model):

    """Pet have an admin URL and link to Pirates"""

    owner = models.ForeignKey(Pirate, null=True, on_delete=models.SET_NULL)


class Ship(models.Model):

    """Ships have an admin URL and are linked to by sailors"""

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Sailor(models.Model):

    """Sailors have an admin URL and sometimes link to ships"""

    name = models.CharField(max_length=80)
    ship = models.ForeignKey(Ship, null=True, on_delete=models.SET_NULL, verbose_name="sea ship")

    @property
    def ship_name(self):
        self.ship.name

    def __str__(self):
        return self.name


class Actor(models.Model):

    """Actors have an admin URL and a many-to-many relationship with movies"""

    name = models.CharField(max_length=80)
    movies = models.ManyToManyField("Movie", related_name="actors")


class Movie(models.Model):

    """Movies have an admin URL and are linked to (m2m) by actors"""

    name = models.CharField(max_length=80)


class Something(models.Model):

    """Somethings don't have an admin URL and are linked to by NotInAdmins"""

    text = models.CharField(max_length=10)


class NotInAdmin(models.Model):

    """NotInAdmins do not have an admin URL and link to Somethings"""

    fk = models.ForeignKey(Something, null=True, on_delete=models.SET_NULL)


class Shape(models.Model):

    """Shapes have a name and a lowercase name property."""

    name = models.CharField(max_length=10)

    @property
    def lower_name(self):
        return self.name.lower()


class Book(models.Model):

    """Book have an admin URL and are linked to images via GenericForeignKey"""

    name = models.CharField(max_length=10)


class Image(models.Model):

    """Image have an admin URL and link to Book via GenericForeignKey"""

    ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    obj_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("ct", "obj_id")


class Journal(models.Model):

    """Journal have an admin URL and are linked to images via GenericForeignKey
    also it have GenericRelation link to Images"""

    name = models.CharField(max_length=10)
    images = GenericRelation(Image)


class Eater(models.Model):

    """Eaters have an admin URL and Meal links to them in two ways."""

    name = models.CharField(max_length=10)


class Meal(models.Model):

    """Meals link to Eaters twice."""

    name = models.CharField(max_length=10)
    prepared = models.ForeignKey(
        Eater,
        related_name="meals_prepared",
        on_delete=models.CASCADE,
    )
    reviewed = models.ForeignKey(
        Eater,
        related_name="meals_reviewed",
        on_delete=models.CASCADE,
    )
