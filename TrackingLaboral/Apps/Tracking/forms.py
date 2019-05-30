from django import forms
from .models import Track
from django.contrib.admin import widgets  


class TrackingForm(forms.ModelForm):

    class Meta:
        model = Track

        fields = [
            'created_at',
        ]
        
        labels = {
            'created_at': 'inicio',
        }

        # widgets = {
        
        #     'start': forms.TimeInput(),
        #     'end': forms.TimeInput(),
        # }

        