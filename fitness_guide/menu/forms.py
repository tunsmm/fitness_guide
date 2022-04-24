from django.forms import ModelForm, TextInput, NumberInput
from .models import Client, Dish, Ingredient, Meal, Product


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("full_name", "sex", "height", "weight",
                  "sport_on_week", "no_eats_days_per_week",
                  "eats_per_day", "phone_number", "type_diet", )

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


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ("name", "recipe", "comments", )

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Название блюда',
                'required': False,
            }),
            "recipe": TextInput(attrs={
                'placeholder': 'Алгоритм приготовления блюда заключается в следующем ... '
            }),
            "comments": TextInput(attrs={
                'placeholder': 'Комментарии'
            }),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ("dish", "product", "measure_scale", "amount")


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ("type_of_meal", "comments", )


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ("name", "calories", "proteins", "fats", "carbohydrates")

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Наименование продукта'
            }),
            "calories": NumberInput(attrs={
                'placeholder': '100'
            }),
            "proteins": NumberInput(attrs={
                'placeholder': '70'
            }),
            "fats": NumberInput(attrs={
                'placeholder': '50'
            }),
            "carbohydrates": NumberInput(attrs={
                'placeholder': '60'
            }),
        }
