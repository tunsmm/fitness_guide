# Generated by Django 4.0.1 on 2022-05-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_daysofmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='type_of_meal',
            field=models.CharField(choices=[('NS', 'Не выбрано'), ('BF', 'Завтрак'), ('LN', 'Полдник'), ('DN', 'Обед'), ('SP', 'Ужин'), ('SN', 'Перекус')], default='NS', max_length=31),
        ),
    ]
