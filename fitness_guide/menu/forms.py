from django.forms import ModelForm, TextInput, NumberInput
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("full_name", "sex", "height", "weight", 
                  "sport_on_week", "no_eats_days_per_week", 
                  "eats_per_day", "phone_number", "type_diet")

        widgets = {
            "full_name": TextInput(attrs={
                'placeholder': 'Иван Иванов'
            }),
            "height": NumberInput(attrs={
                'placeholder': '180'
            }),
            "weight": NumberInput(attrs={
                'placeholder': '70'
            }),
            "sport_on_week": NumberInput(attrs={
                'placeholder': '3'
            }),
            "no_eats_days_per_week": NumberInput(attrs={
                'placeholder': '1'
            }),
            "eats_per_day": NumberInput(attrs={
                'placeholder': '3'
            }),
            "phone_number": TextInput(attrs={
                'placeholder': '8 (987) 654 32 10'
            }),
            "type_diet": TextInput(attrs={
                'placeholder': 'health'
            }),
        }
