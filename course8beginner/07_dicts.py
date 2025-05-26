my_dict = dict()
my_other_dict = {}
print(type(my_dict))

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Switf", "Kotlin"},
    1: 1.77
}  # seria como obj js - json
print(my_dict)
print(len(my_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])
print(my_dict[1])
my_dict["Calle"] = "Calle Moure"
print(my_dict)
del my_dict["Calle"]
print(my_dict)
print("Moure" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
# Crear un dic con valores vacios
my_new_dict = my_dict.fromkeys(("Nombres", 1))
print(my_new_dict)
