# Generated by Django 4.0.1 on 2022-04-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_day_meal_mealsofday_dishesofmeal'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='type_of_meal',
            field=models.CharField(choices=[('NS', 'Не установлено'), ('BF', 'Завтрак'), ('LN', 'Обед'), ('DN', 'Ужин'), ('SP', 'SP'), ('SN', 'Перекус')], default='NS', max_length=31),
        ),
    ]
