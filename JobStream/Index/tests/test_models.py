from django.test import TestCase

from model_bakery import baker


class IndexModelTest(TestCase):
    """Bake an Index model to run tests on."""

    def test_index_model_existence(self):
        """
        :return: True if the baked model is correctly constructed, False otherwise.
        """
        pass

    def test_index_has_id(self):
        """
        :return: True if the baked model has auto created an ID field, False otherise.
        """
        pass

    def test_index_has_title(self):
        """
        :return: True if the baked model has a title, False otherwise
        """
        pass

    def test_index_has_summary(self):
        """
        :return: True if the baked model has a summary, False otherwise
        """
        pass

    def test_index_has_small_or_big_text(self):
        """
        :return: True if the baked model has either a small or big text field, False if neither are present.
        """
        pass

    def test_index_str(self):
        """
        :return: The human-readable form of the baked model.
        """
        pass