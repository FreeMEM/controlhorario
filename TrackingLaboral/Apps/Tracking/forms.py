from django import forms
from .models import Track


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
            'start': forms.TimeInput(attrs={'class':'form-control'}),
            'end': forms.TimeInput(attrs={'class':'form-control'}),
        }