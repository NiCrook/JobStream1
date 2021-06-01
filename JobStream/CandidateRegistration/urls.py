from django.urls import path
from . import views

urlpatterns = [
    path('candidate_registration_base_user/',
         ...,
         name='base candidate registration'),
    path('candidate_registration_base_user=success',
         ...,
         name='base candidate registration success'),
    path('candidate_registration_base_user=success/candidate_profile_creation',
         ...,
         name='candidate profile creation'),
]