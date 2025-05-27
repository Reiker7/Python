# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print(my_condition)

while my_condition < 20:
    my_condition += 2
    print(my_condition)

    if my_condition == 16:
        print("He pasado por 16")
        break  # Con el break rompo la ejecución
# Tmb Existe Continue es como un break rompe la ejecución pero continua el for

# For
my_list = [32, 40, 17, 24, 30, 30]
my_tuple = (35, 1.77, "Brais", "Mouse", "Brais")
my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Switf", "Kotlin"},
    1: 1.77
}

for element in my_list:
    print(element)

for element in my_tuple:
    print(element)

for element in my_dict:  # solo imprime clave
    print(element)

for element in my_dict.values():  # solo imprime clave
    print(element)
