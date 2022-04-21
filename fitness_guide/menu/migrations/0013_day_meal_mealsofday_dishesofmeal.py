# Generated by Django 4.0.1 on 2022-04-15 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_alter_ingredient_dish_alter_ingredient_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дни',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Прием пищи',
                'verbose_name_plural': 'Приемы пищи',
            },
        ),
        migrations.CreateModel(
            name='MealsOfDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.day')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.meal')),
            ],
            options={
                'unique_together': {('day', 'meal')},
            },
        ),
        migrations.CreateModel(
            name='DishesOfMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.dish')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.meal')),
            ],
            options={
                'unique_together': {('meal', 'dish')},
            },
        ),
    ]
