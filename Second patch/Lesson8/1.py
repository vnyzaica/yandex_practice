# напишите код функции print_valid_cities, которая
# принимает аргументы all_cities и used_cities
def print_valid_cities(full,use):
    print (", ".join(full.difference(use)))

all_cities = set([
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
])

used_cities = set(['Калуга', 'Абакан' , 'Новосибирск'])


print_valid_cities(all_cities, used_cities)

