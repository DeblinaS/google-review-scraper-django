from django import forms
from django.forms import CharField, ModelMultipleChoiceField, ModelChoiceField

class LoginForm(forms.Form):
   url = forms.URLField(required=True)
   number = forms.IntegerField(required=True)
   file=forms.CharField(required=True)