import os


def cook_book_dict():
    """Преобразовывает текстовый файл в словарь, не перезаписывая сам файл"""
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as file:
        for line in file:
            dish_ingredients = []
            number_ingredients = int(file.readline())
            for i in range(1, number_ingredients + 1):
                ingredients = file.readline().split(' | ')
                dish_ingredients.append({'ingredient_name': ingredients[0], 'quantity': ingredients[1],
                                         'measure': ingredients[2].strip()})
            cook_book[line.strip()] = dish_ingredients
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """На вход принимает список блюд из cook_book и количество персон для кого мы будем готовить.
    На выходе получает словарь с названием ингредиентов и его количества для блюда"""
    cook_book = cook_book_dict()
    required_ingredients = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in required_ingredients.keys():
                required_ingredients[ingredients['ingredient_name']] = \
                    {'measure': ingredients['measure'], 'quantity': int(ingredients['quantity']) * person_count}
            else:
                required_ingredients[ingredients['ingredient_name']]['quantity'] += \
                    int(ingredients['quantity']) * person_count
    return required_ingredients


print(cook_book_dict())
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


def getting_data_and_writing_list(files):
    """Преобразовывает считанные данные в список"""
    data = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            data.append([file, len(lines)])
            data[len(data) - 1] += lines
    data.sort(key=len)
    return data


def writing_data_in_file(necessary_data, necessary_file):
    """Записывает в новый файл информацию"""
    with open('final.txt', 'w', encoding='utf-8') as f:
        for file in necessary_data:
            for el in file:
                f.write(f'{el}\n')
    file_path = os.path.join(os.getcwd(), necessary_file)
    return file_path


print(writing_data_in_file(getting_data_and_writing_list(['1.txt', '2.txt', '3.txt']), 'final.txt'))





