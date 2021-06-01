from django.urls import path
from . import views

urlpatterns = [
    path('organization_registration_base_user',
         ...,
         name='base org registration'),
    path('organization_registration_base_user=success',
         ...,
         name='base org registration=success'),
    path('organization_registration_base_user=success/organization_profile_creation',
         ...,
         name=' org profile creation'),
]