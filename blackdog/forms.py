from django import forms

from .models import Bark


class BarkForm(forms.ModelForm):
    class Meta:
        model = Bark
        fields = ['content']
    
    def clean_views(self):
        """Every new form or updated form is submitted we reset the counter"""
        return 0
    