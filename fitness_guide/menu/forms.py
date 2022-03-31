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
                'placeholder': 'Полное имя'
            }),
            "height": NumberInput(attrs={
                'placeholder': '180'
            })
        }
