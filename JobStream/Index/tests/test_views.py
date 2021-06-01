from django.test import TestCase
from django.urls import reverse

from model_bakery import baker


class IndexViewTest(TestCase):
    """Tests for the Index page."""

    def test_index_view_url_exists_at_right_location(self):
        """
        Test the URL routing to Index page.
        :return: True if the URL routing is correct, False otherwise.
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_index_articles_exist(self):
        """
        Check to see if any Articles exist on the Index page.
        :return: True if an Article exists on the index page, False otherwise.
        """

    def test_index_articles_stream(self):
        """
        Check to see if the correct number of Articles exist on the Index page.
        :return: True if the correct number of Articles exist on the Index page, False otherwise.
        """


class AboutViewTest(TestCase):
    """Tests for the About page."""

    def test_about_view_url_exists_at_right_location(self):
        """
        Test the URL routing to the About page.
        :return: True if the URL routing is correct, False otherwise.
        """
        response = self.client.get('about/')
        self.assertEqual(response.status_code, 200)
