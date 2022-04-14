from django.contrib import admin

# Register your models here.

from .models import Client, Dish, Ingredient, MeasureScale, MeasureScaleCourse, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "full_name", "sex", "type_diet", "sport_on_week", "no_eats_days_per_week", "eats_per_day")
    search_fields = ("type_diet", "sex", )
    list_filter = ("sport_on_week", "no_eats_days_per_week", "eats_per_day", )
    empty_value_display = "-пусто-"


class DishAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "recipe", "comments")
    search_fields = ("name", )
    empty_value_display = "-пусто-"


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("dish", "product", "measure_scale", "amount", )
    search_fields = ("dish", "product", "measure_scale", )
    list_filter = ("measure_scale", )
    empty_value_display = "-пусто-"


class MeasureScaleAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "shortname")
    empty_value_display = "-пусто-"


class MSCoursesAdmin(admin.ModelAdmin):
    list_display = ("ms_from", "ms_to", "value")
    search_fields = ("ms_from", "ms_to", )
    list_filter = ("ms_from", "ms_to", )
    empty_value_display = "-пусто-"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "calories", "proteins", "fats", "carbohydrates")
    search_fields = ("name", )
    list_filter = ("calories", )
    empty_value_display = "-пусто-"


admin.site.register(Client, ClientAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MeasureScale, MeasureScaleAdmin)
admin.site.register(MeasureScaleCourse, MSCoursesAdmin)
admin.site.register(Product, ProductAdmin)
