from __future__ import unicode_literals
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django_webtest import WebTest

from relatives.utils import edit_link
from .models import Pirate, Ship, Sailor


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


class TemplateFilterTest(WebTest):
    def setUp(self):
        self.user = User.objects.create_superuser('u', 'u@example.com', 'pass')

    def login(self):
        form = self.app.get(reverse('admin:index')).form
        form['username'] = self.user.username
        form['password'] = 'pass'
        return form.submit()

    def test_foreign_key(self):
        self.login()
        ship = Ship.objects.create(id=1, name="Star of India")
        sailor = Sailor.objects.create(name="John Ford", ship=ship)
        response = self.app.get(reverse('admin:tests_sailor_change',
                                        args=[sailor.id]))
        self.assertIn('<a href="/adm/tests/ship/1/">Star of India</a>',
                      response.unicode_normal_body)

    def test_no_foreign_key(self):
        self.login()
        ship = Ship.objects.create(id=1, name="Star of India")
        response = self.app.get(reverse('admin:tests_ship_change',
                                        args=[ship.id]))
        self.assertIn('<p>Star of India</p>', response.unicode_normal_body)
