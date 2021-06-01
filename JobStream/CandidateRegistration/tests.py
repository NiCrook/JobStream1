from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from model_bakery import baker

from ..models import Listings, Candidates


class CandidatesBakerTest(TestCase):

    def test_candidate_bake(self):
        listing = baker.make('Listings')
        candidate = baker.make('Candidates')
        self.assertTrue(isinstance(listing, Listings))
        self.assertTrue(isinstance(candidate, Candidates))