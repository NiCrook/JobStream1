from django.shortcuts import render

# from .models import Listings, Candidates


def home(request):
    return render(request, 'base.html')  # TODO make html reference. do I need to add forms?


def employer_sign_in(request):
    return render(request, '')  # TODO make html reference, add in ability to sign up or request new password


def employer_sign_in_success(request):
    return render(request, '')  # TODO make html reference, this is to be a redirect and also to redirect


def employer_sign_in_failure(request):
    return render(request, '')  # TODO make html reference, is it possible to merge this with sign_in_success?


def employer_home(request, employer_id):
    return render(request, '')  # TODO make html reference


def employer_post_listing(request):
    return render(request, '')  # TODO make html reference


def candidate_pool(request):
    return render(request, '')  # TODO make html reference


def about(request):
    return render(request, 'about.html')
