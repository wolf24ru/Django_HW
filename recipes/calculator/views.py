from django.shortcuts import render

DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
        # можете добавить свои рецепты ;)
    }

def home(request):
    dish_list = [dish for dish in DATA]
    context = {
        'menu': dish_list
    }
    return render(request, 'calculator/home.html', context)


def dishes(request, dish):
    if dish in DATA:
        num_persons = int(request.GET.get('servings', 1))
        count_ingredient = {ingredient: number * num_persons for ingredient, number in DATA[dish].items()}
        return render(request, 'calculator/index.html', {
            'dish': count_ingredient
        })
    else:
        return render(request, 'calculator/index.html',)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
