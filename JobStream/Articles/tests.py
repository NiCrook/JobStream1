from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from model_bakery import baker

from ..models import Listings, Candidates


class ListingsBakerTest(TestCase):

    def test_listing_bake(self):
        listing = baker.make('Listings')
        self.assertTrue(isinstance(listing, Listings))
        self.assertEqual(listing.__str__(), (str(listing.position_title) + " by " + str(listing.company)))