# Generated by Django 4.0.1 on 2022-04-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_dish_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.IntegerField()),
                ('product', models.IntegerField()),
                ('amount', models.FloatField()),
                ('measure_scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.measurescale')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'unique_together': {('dish', 'product')},
            },
        ),
        migrations.RenameModel(
            old_name='MeasureScaleCourses',
            new_name='MeasureScaleCourse',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
    ]
