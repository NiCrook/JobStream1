from django.contrib.auth.models import User
from django.db import models

# from ..CandidateRegistration.models import Candidate
import "Job Stream"


class Agent(models.Model):
    """Model for Agents (recruiters), linked to their base User profile, created at registration.
    Shows which organization they are currently linked with, if currently linked with an organization.
    Show public email which Candidates can send their resume and any other related docs to."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    with_org = models.BooleanField(default=False)
    at_org = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    public_email = models.EmailField()
