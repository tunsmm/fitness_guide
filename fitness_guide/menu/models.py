from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

User = get_user_model()


class Client(models.Model):
    full_name = models.TextField()
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    sex = models.BooleanField()
    sport_on_week = models.SmallIntegerField()
    no_eats_days_per_week = models.SmallIntegerField()
    eats_per_day = models.SmallIntegerField()
    phone_number = models.TextField()
    type_diet = models.TextField()
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return f"/client/{self.id}"
    
    

class Menu(models.Model):
    comments = models.TextField(blank=True)


class Day(models.Model):
    comments = models.TextField(blank=True)
    

class Meal(models.Model):
    comments = models.TextField(blank=True)
    

class Product(models.Model):
    calories = models.SmallIntegerField()
    proteins = models.SmallIntegerField()
    fats = models.SmallIntegerField()
    carbohydrates = models.SmallIntegerField()
    
    
class Measure_scale(models.Model):
    name = models.TextField()
    shortname = models.TextField()
    

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
    
    
class Restricted_Product(models.Model):
    class Meta:
        unique_together = (('client', 'product'),)

    client = models.IntegerField()
    product = models.IntegerField()
    score = models.CharField(max_length=2, default=None)
    
    
class Loved_Product(models.Model):
    class Meta:
        unique_together = (('client', 'product'),)

    client = models.IntegerField()
    product = models.IntegerField()
    score = models.CharField(max_length=2, default=None)


class Ingredients(models.Model):
    class Meta:
        unique_together = (('dish', 'product'),)

    dish = models.IntegerField()
    product = models.IntegerField()
    ms = models.ForeignKey(Measure_scale, on_delete=models.CASCADE)


class Dishes_Of_Meal:
    class Meta:
        unique_together = (('meal', 'dish'),)

    dish = models.IntegerField()
    meal = models.IntegerField()
    comments = models.TextField(blank=True)
    
    
class Meals_Of_Day:
    class Meta:
        unique_together = (('day', 'meal'),)

    day = models.IntegerField()
    meal = models.IntegerField()
    comments = models.TextField(blank=True)
    

class Days_Of_Menu:
    class Meta:
        unique_together = (('menu', 'day'),)

    day = models.IntegerField()
    menu = models.IntegerField()
    comments = models.TextField(blank=True)
    
    
class Ms_Courses:
    class Meta:
        unique_together = (('ms_from', 'ms_to'),)

    ms_from = models.IntegerField()
    ms_to = models.IntegerField()
    value = models.IntegerField()
    
    