from django.contrib.auth.models import User
from django.db import models


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25)
    currently_employed = models.BooleanField(default=False)
    employed_at = models.CharField(max_length=150, null=True)