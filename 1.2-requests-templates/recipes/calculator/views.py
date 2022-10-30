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
    'apple_pie': {
        'яйца, шт': 4,
        'ванилин, пакетик': 1,
        'сахар, г': 250,
        'мука, г': 250,
    },
}

def recipe_view(request, recipe='omlet'):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    dict = DATA[recipe].copy()
    for ingredient in dict.keys():
        dict[ingredient] = dict[ingredient] * servings
    return render(request, template_name, {'recipe': dict})

