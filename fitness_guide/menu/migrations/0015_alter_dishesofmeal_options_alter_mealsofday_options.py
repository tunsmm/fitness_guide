# Generated by Django 4.0.1 on 2022-04-15 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_meal_type_of_meal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishesofmeal',
            options={'verbose_name': 'Блюдо в приеме пищи', 'verbose_name_plural': 'Блюда в приеме пищи'},
        ),
        migrations.AlterModelOptions(
            name='mealsofday',
            options={'verbose_name': 'Прием пищи в день', 'verbose_name_plural': 'Приемов пищи в день'},
        ),
    ]
