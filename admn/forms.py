from django import forms

from admn.models import users


class newuser(forms.ModelForm):
    class Meta:
        model = users
        fields = ['username','password']