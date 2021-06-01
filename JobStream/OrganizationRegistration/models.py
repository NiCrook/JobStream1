from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    """Models for Organizations, linked to the creator's base User profile, created at registration.
    Show name, phone #, email, sector, and industry, to public views."""
    SECTOR_CHOICES = {}
    INDUSTRY_CHOICES = {}

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    location = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)
    sector = models.CharField()
    industry = models.CharField()
