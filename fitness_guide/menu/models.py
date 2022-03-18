from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# This block contains models in which there are no foreign keys

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
    poll = models.ForeignKey(Menu, on_delete=models.CASCADE)
    type_diet = models.CharField(max_length=20)
    comments = models.TextField(blank=True)
    
# This block contains models in which the composite primary key