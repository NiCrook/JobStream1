from django import forms


class BaseAgentRegistrationFrom(forms.Form):

    username = forms.CharField()