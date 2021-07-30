# напишите здесь функцию print_shopping_list(),
# подобрав уникальные названия продуктов и сложив значения
def print_shopping_list(food1,food2):
    dish1=food1.values()
    dish2=food2.values()
    food12=set(food1)
    food22=set(food2)
    unical_food = food12.union(food22)
    for uni_food in unical_food:
        sum = 0
        if uni_food in food1:
            sum = sum + food1[uni_food]
            if uni_food in food2:
                sum = sum + food2[uni_food]
        else:
            sum = sum + food2[uni_food]
        print(uni_food + ": " +str(sum))
            
    #print(", ".join(unical_food))# напишите здесь свою функцию
    

pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)

