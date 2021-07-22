friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}
friends['Станислав'] = 'СПБ'
friends['Я'] = 'Здесь'
for name, city in friends.items():
    print(name + " живёт в городе " + city)
    
