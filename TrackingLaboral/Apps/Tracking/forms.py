from django import forms
from .models import Track
from django.contrib.admin import widgets  


class TrackingForm(forms.ModelForm):

    class Meta:
        model = Track

        fields = [
            'start',
            'end',
        ]
        
        labels = {
            'start': 'inicio',
            'end': 'fin', 
        }

        widgets = {
            # 'start': forms.DateInput(),
            # 'end': forms.DateInput(),
            'start': forms.TimeInput(),
            'end': forms.TimeInput(),
        }

        initial = {
            'start' : "21:00",
            'end' : "20:00"
        }