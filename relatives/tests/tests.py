from __future__ import unicode_literals
from django.test import TestCase

from relatives.utils import edit_link
from .models import Pirate, Ship


class EditLinkTest(TestCase):

    def test_no_admin_url(self):
        pirate = Pirate.objects.create(id=1, name="Lowell Taylor")
        self.assertEqual(edit_link(pirate), "Lowell Taylor")

    def test_with_primary_key(self):
        ship = Ship.objects.create(id=1, name="Star of India")
        self.assertEqual(edit_link(ship),
                         '<a href="/adm/tests/ship/1/">Star of India</a>')

    def test_no_primary_key(self):
        ship = Ship(name="Star of India")
        self.assertEqual(edit_link(ship), "Star of India")
