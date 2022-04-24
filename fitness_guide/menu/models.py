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


class RestrictedProduct(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.CharField(max_length=1, default=1)

    class Meta:
        unique_together = (('client', 'product'),)
        verbose_name = 'Запрещенный продукт'
        verbose_name_plural = 'Запрещенные продукты'


class LovedProduct(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.CharField(max_length=1, default=1)

    class Meta:
        unique_together = (('client', 'product'),)
        verbose_name = 'Любимый продукт'
        verbose_name_plural = 'Любимые продукты'


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


class Meal(models.Model):
    NOT_SET = 'NS'
    BREAKFAST = 'BF'
    LUNCH = 'LN'
    DINNER = 'DN'
    SUPPER = 'SP'
    SNACK = 'SN'

    TYPE_OF_MEALS = [
        (NOT_SET, 'Не выбрано'),
        (BREAKFAST, 'Завтрак'),
        (LUNCH, 'Полдник'),
        (DINNER, 'Обед'),
        (SUPPER, 'Ужин'),
        (SNACK, 'Перекус'),
    ]

    type_of_meal = models.CharField(
        max_length=31,
        choices=TYPE_OF_MEALS,
        default=NOT_SET,
    )
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Прием пищи'
        verbose_name_plural = 'Приемы пищи'

    def __str__(self):
        return f"{self.id} {self.get_type_of_meal_display()}"


class DishesOfMeal(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    comments = models.TextField(blank=True)

    class Meta:
        unique_together = (('meal', 'dish'),)
        verbose_name = 'Блюдо в приеме пищи'
        verbose_name_plural = 'Блюда в приеме пищи'


class Day(models.Model):
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class MealsOfDay(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    comments = models.TextField(blank=True)

    class Meta:
        unique_together = (('day', 'meal'),)
        verbose_name = 'Прием пищи в день'
        verbose_name_plural = 'Приемов пищи в день'


class Menu(models.Model):
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class DaysOfMenu(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    comments = models.TextField(blank=True)

    class Meta:
        unique_together = (('menu', 'day'),)
        verbose_name = 'День в меню'
        verbose_name_plural = 'Дни в меню'


class Template(models.Model):
    NOT_SET = 'not_set'
    LOSS = 'loss'
    HEALTH = 'health'
    GAIN = 'gain'

    TYPE_OF_DIET = [
        (NOT_SET, 'Не выбрано'),
        (LOSS, 'Похудение'),
        (HEALTH, 'Сбалансированное питание'),
        (GAIN, 'Набор массы'),
    ]

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    type_diet = models.CharField(
        max_length=20,
        choices=TYPE_OF_DIET,
        default=NOT_SET
    )
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


class Result(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    factor = models.FloatField(default=1)

    class Meta:
        unique_together = (('client', 'template'),)
        verbose_name = 'Шаблон для клиента'
        verbose_name_plural = 'Шаблоны для клиентов'
