from datetime import date

from django import forms
from cosmetica.models import Cosmetica


class CosmeticaForm(forms.ModelForm):
    class Meta:
        model = Cosmetica
        fields = '__all__'


        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data rezervari', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere', 'rows': 3}),

        }

        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data


class CosmeticaUpdateForm(forms.ModelForm):
    class Meta:
        model = Cosmetica
        fields = '__all__'

        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere', 'rows': 3}),

        }