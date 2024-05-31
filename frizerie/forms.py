from datetime import date

from django import forms


from frizerie.models import Frizerie


class FrizerieForm(forms.ModelForm):

    class Meta:
        model = Frizerie
        fields = '__all__'


        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data rezervari', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere', 'rows': 3}),

        }