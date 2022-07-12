from ..models import DaysOfMenu, DishesOfMeal, Ingredient, MealsOfDay, Menu


def menu_shower(menu_id):
    menu_detail = {}
    menu = Menu.objects.get(id=menu_id)
    menu_detail['id'] = menu_id
    menu_detail['comments'] = menu.comments
    day_list = list(DaysOfMenu.objects.select_related('day').filter(menu=menu))
    menu_detail['days'] = []

    # Create info about days
    for day_index, day in enumerate(day_list):
        menu_detail['days'].append({})
        menu_detail['days'][day_index]['daysofmenu_id'] = day.id  # ID of row in DaysOfMenu
        menu_detail['days'][day_index]['id'] = day.day_id
        menu_detail['days'][day_index]['name'] = str(day.day)
        menu_detail['days'][day_index]['comments'] = day.day.comments

        # Create info about meals in day
        meals_in_day = menu_detail['days'][day_index]['meals'] = []
        meal_list = list(MealsOfDay.objects.select_related('meal').filter(day=day.day.id))
        for meal_index, meal in enumerate(meal_list):
            meals_in_day.append({})
            meals_in_day[meal_index]['id'] = meal.meal_id
            meals_in_day[meal_index]['name'] = str(meal.meal)
            meals_in_day[meal_index]['comments'] = meal.meal.comments

            # Create info about dishes in meal
            dishes_in_meal = meals_in_day[meal_index]['dishes'] = []
            dish_list = list(DishesOfMeal.objects.select_related('dish').filter(meal=meal.meal.id))
            for dish_index, dish in enumerate(dish_list):
                dishes_in_meal.append({})
                dishes_in_meal[dish_index]['id'] = dish.dish_id
                dishes_in_meal[dish_index]['name'] = str(dish.dish)
                dishes_in_meal[dish_index]['recipe'] = dish.dish.recipe
                dishes_in_meal[dish_index]['comments'] = dish.dish.comments

                # Create info about products in dish (ingredients)
                ingredients = dishes_in_meal[dish_index]['ingredients'] = []
                ingredient_list = list(Ingredient.objects.select_related('product').filter(dish=dish.dish.id))
                for ingredient_index, ingredient in enumerate(ingredient_list):
                    ingredients.append({})
                    ingredients[ingredient_index]['id'] = ingredient.id
                    ingredients[ingredient_index]['name'] = str(ingredient.product)
                    ingredients[ingredient_index]['amount'] = ingredient.amount
                    ingredients[ingredient_index]['measure_scale'] = ingredient.measure_scale.shortname

    return menu_detail
