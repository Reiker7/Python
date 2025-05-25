# Variables
my_string_variable = "My String variable"
my_int_variable = 5
my_bool_variable = False
# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

print(type(my_int_variable))
# guardo el valor de int y lo cambio a string
my_int_variable = str(my_int_variable)
print(type(my_int_variable))
# Algunas funciones del sistema (len)
print(len(my_string_variable))  # marca la longitud
# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print(name, surname, age, "Mi alias es:", alias)
# Inputs
a = int(input("primer numero"))
b = int(input("segundo numero"))
c = (a**2 + b**2) ** 0.5  # ** 0.5 para raiz cuadrada
print(c)
# Forzamos tipo?
adress: str = 'mi dirección'
adress = 32  # y no respetara lo ant y cambiara a int
