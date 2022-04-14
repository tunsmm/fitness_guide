from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    sex = models.BooleanField()
    sport_on_week = models.SmallIntegerField()
    no_eats_days_per_week = models.SmallIntegerField()
    eats_per_day = models.SmallIntegerField()
    phone_number = models.CharField(max_length=15)
    type_diet = models.CharField(max_length=31)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f"/client/{self.id}"

"""

class Menu(models.Model):
    comments = models.TextField(blank=True)


class Day(models.Model):
    comments = models.TextField(blank=True)


class Meal(models.Model):
    comments = models.TextField(blank=True)

"""

class Product(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product"


class MeasureScale(models.Model):
    name = models.CharField(max_length=255)
    shortname = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Шкала измерения'
        verbose_name_plural = 'Шкалы измерения'

    def __str__(self) -> str:
        return self.name


class MeasureScaleCourse(models.Model):
    ms_from = models.IntegerField()
    ms_to = models.IntegerField()
    value = models.FloatField()

    class Meta:
        unique_together = (('ms_from', 'ms_to'),)
        verbose_name = 'Курс шкал'
        verbose_name_plural = 'Курсы шкал'


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=True)
    recipe = models.TextField(blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    measure_scale = models.ForeignKey(MeasureScale, on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        unique_together = (('dish', 'product'),)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f"{self.dish}-{self.product}"

"""

# This block contains models that have a primary key and a foreign key

class Template(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    type_diet = models.CharField(max_length=20)
    comments = models.TextField(blank=True)


# This block contains models in which the composite primary key

class Result(models.Model):
    class Meta:
        unique_together = (('client', 'template'),)

    template = models.IntegerField()
    client = models.IntegerField()
    factor = models.IntegerField(default = 1)


class RestrictedProduct(models.Model):
    class Meta:
        unique_together = (('client', 'product'),)

    client = models.IntegerField()
    product = models.IntegerField()
    score = models.CharField(max_length=2, default=None)


class LovedProduct(models.Model):
    class Meta:
        unique_together = (('client', 'product'),)

    client = models.IntegerField()
    product = models.IntegerField()
    score = models.CharField(max_length=2, default=None)

class DishesOfMeal:
    class Meta:
        unique_together = (('meal', 'dish'),)

    dish = models.IntegerField()
    meal = models.IntegerField()
    comments = models.TextField(blank=True)


class MealsOfDay:
    class Meta:
        unique_together = (('day', 'meal'),)

    day = models.IntegerField()
    meal = models.IntegerField()
    comments = models.TextField(blank=True)


class DaysOfMenu:
    class Meta:
        unique_together = (('menu', 'day'),)

    day = models.IntegerField()
    menu = models.IntegerField()
    comments = models.TextField(blank=True)

"""
