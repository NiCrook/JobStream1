from django.urls import path
from . import views

urlpatterns = [
    path(
        'agent_registration_base_user/',
        ...,
        name='base agent registration'),
    path(
        'agent_registration_base_user=success',
        ...,
        name='base agent registration success'),
    path('agent_registration_base_user=success/agent_profile_creation',
         ...,
         'agent profile creation'),
]