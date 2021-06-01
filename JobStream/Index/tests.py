from django.test import TestCase
from django.urls import reverse

from model_bakery import baker


class HomeViewTest(TestCase):

    def test_home_view_url_exists_at_right_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class AboutViewTest(TestCase):

    def test_about_view_url_exists_at_right_location(self):
        response = self.client.get('about/')
        self.assertEqual(response.status_code, 200)
