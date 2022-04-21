from django.contrib import admin

from .models import Client, Day, DaysOfMenu, Dish, DishesOfMeal, Ingredient, LovedProduct, Meal, MealsOfDay
from .models import MeasureScale, MeasureScaleCourse, Menu, Product, RestrictedProduct, Result, Template


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "full_name", "sex", "type_diet", "sport_on_week", "no_eats_days_per_week", "eats_per_day")
    search_fields = ("type_diet", "sex", )
    list_filter = ("sport_on_week", "no_eats_days_per_week", "eats_per_day", )
    empty_value_display = "-пусто-"


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ("pk", "comments")
    empty_value_display = "-пусто-"


@admin.register(DaysOfMenu)
class DaysOfMenuAdmin(admin.ModelAdmin):
    list_display = ("pk", "day", "menu", "comments")
    empty_value_display = "-пусто-"


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "recipe", "comments")
    search_fields = ("name", )
    empty_value_display = "-пусто-"


@admin.register(DishesOfMeal)
class DishesOfMealAdmin(admin.ModelAdmin):
    list_display = ("pk", "dish", "meal", "comments")
    empty_value_display = "-пусто-"


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "dish", "product", "measure_scale", "amount", )
    search_fields = ("dish", "product", "measure_scale", )
    list_filter = ("measure_scale", )
    empty_value_display = "-пусто-"


@admin.register(LovedProduct)
class LovedProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "client", "product", "score")
    empty_value_display = "-пусто-"


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("pk", "type_of_meal", "comments")
    empty_value_display = "-пусто-"


@admin.register(MealsOfDay)
class MealsOfDayAdmin(admin.ModelAdmin):
    list_display = ("pk", "day", "meal", "comments")
    empty_value_display = "-пусто-"


@admin.register(MeasureScale)
class MeasureScaleAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "shortname")
    empty_value_display = "-пусто-"


@admin.register(MeasureScaleCourse)
class MSCourseAdmin(admin.ModelAdmin):
    list_display = ("ms_from", "ms_to", "value")
    search_fields = ("ms_from", "ms_to", )
    list_filter = ("ms_from", "ms_to", )
    empty_value_display = "-пусто-"


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("pk", "comments")
    empty_value_display = "-пусто-"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "calories", "proteins", "fats", "carbohydrates")
    search_fields = ("name", )
    list_filter = ("calories", )
    empty_value_display = "-пусто-"


@admin.register(RestrictedProduct)
class ResctrictedProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "client", "product", "score")
    empty_value_display = "-пусто-"


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("pk", "client", "template", "factor")
    empty_value_display = "-пусто-"


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("pk", "menu", "type_diet", "comments")
    empty_value_display = "-пусто-"
