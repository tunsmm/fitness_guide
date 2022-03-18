from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

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
    

class Menu(models.Model):
    comments = models.TextField()


class Day(models.Model):
    comments = models.TextField()
    

class Meal(models.Model):
    comments = models.TextField()
    

class Product(models.Model):
    calories = models.SmallIntegerField()
    proteins = models.SmallIntegerField()
    fats = models.SmallIntegerField()
    carbohydrates = models.SmallIntegerField()
    
    
class Measure_scale(models.Model):
    name = models.TextField()
    shortname = models.TextField()
    