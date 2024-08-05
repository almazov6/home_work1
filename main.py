def cook_book():
    with open('cook_book.txt') as file:
        cook_book = {}
        for i in file:
            cook_name = i.strip()
            ingr_count = file.readline()
            ingredients = []
            for p in range(int(ingr_count)):
                recepie = file.readline().strip().split(' | ')
                ingredient_name, quantity, measure = recepie
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            file.readline()
            cook_book.update({cook_name: ingredients})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    dict_book = dict()
    for i in dishes:
      for k in range(len(cook_book()[i])):
        if cook_book()[i][k]['ingredient_name'] in dict_book:
          dict_book[cook_book()[i][k]['ingredient_name']]['quantity'] = (
                  dict_book[cook_book()[i][k]['ingredient_name']]['quantity'] + cook_book()[i][k]['quantity'] * person_count)
        else:
          dict_book.update({
            cook_book()[i][k]['ingredient_name']: {'measure': cook_book()[i][k]['measure'],
            'quantity': cook_book()[i][k]['quantity'] * person_count}
          })
    print(dict_book)


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)