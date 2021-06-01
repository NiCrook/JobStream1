from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

from ..AgentRegistration.models import Agent
from ..OrganizationRegistration.models import Organization


class Listings(models.Model):
    posted_by = models.ForeignKey(Agent, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    slug = models.SlugField()
    position_title = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    remote = models.BooleanField(default=False)
    pay_rate = models.CharField(max_length=150, blank=True)
    content = RichTextField()
    updated = models.DateTimeField(auto_now=True)
    candidates = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    datetime_deleted = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        slug = str(self.datetime) + ' ' + str(self.org)
        self.listing_slug = slugify(slug)

    def __str__(self):
        return f"{self.position_title} by {self.org}"
