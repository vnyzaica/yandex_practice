def print_shopping_list(food1,food2):
    food1=set(food1)
    food2=set(food2)
    print(", ".join(food1.union(food2)))# напишите здесь свою функцию


pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print_shopping_list(pizza, salad)
