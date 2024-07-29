from datetime import date

from django import forms

from coafor.models import Coafor



class CoaforForm(forms.ModelForm):
    class Meta:
        model = Coafor
        fields = '__all__'


        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),

            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere', 'rows': 3}),

        }

        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data




class CoaforUpdateForm(forms.ModelForm):
    class Meta:
        model = Coafor
        fields = '__all__'


        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere', 'rows': 3}),

        }