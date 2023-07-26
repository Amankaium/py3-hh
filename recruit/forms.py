from django import forms
from .models import Recruiter


class RecruiterUpdateForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude = ['user']
