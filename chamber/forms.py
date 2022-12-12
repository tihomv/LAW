from .models import Case
from django import forms
from django.core.exceptions import ValidationError


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ("title", "text")

    # def clean_title(self):
    #     title = self.cleaned_data["title"]
    #     if 'Django' not in title:
    #         raise ValidationError("ERROR")
    #     return title
