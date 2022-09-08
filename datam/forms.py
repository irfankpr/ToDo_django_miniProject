from django import forms

from datam.models import todo


class newtask(forms.ModelForm):
     class Meta:
         model = todo
         fields = ['task']