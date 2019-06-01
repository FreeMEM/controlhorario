from django import forms
from .models import Track
from django.contrib.admin import widgets  

from datetime import datetime


class TrackingForm(forms.ModelForm):

    class Meta:
        model = Track

        fields = [
            'created_at',
        ]
        
        labels = {
            'created_at': 'inicio',
        }
        
        initial={'created_at': datetime.now()}
        # widgets = {
        
        #     'start': forms.TimeInput(),
        #     'end': forms.TimeInput(),
        # }

        