from django.contrib import admin

# Register your models here.

from .models import Client, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "full_name", "sex", "type_diet", "sport_on_week", "no_eats_days_per_week", "eats_per_day")
    search_fields = ("type_diet", "sex",)
    list_filter = ("sport_on_week", "no_eats_days_per_week", "eats_per_day",)
    empty_value_display = "-пусто-"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "calories", "proteins", "fats", "carbohydrates")
    search_fields = ("name",)
    list_filter = ("calories", )
    empty_value_display = "-пусто-"


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
