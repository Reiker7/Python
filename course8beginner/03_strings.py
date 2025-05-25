my_string = "Mi String"
my_string2 = "Mi otro String"
print(len(my_string))
print(my_string + " " + my_string2)
print("mi salto\nde línea")  # salto de linea
print("mi salto\tde línea")  # tabulación
# formateo
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {}, {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s, %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name}, {surname} y mi edad es {age}")  # Mejor
# Desempaquetado de caracteres
languaje = "Python"
a, b, c, d, e, f = languaje
print(a)
print(b)
print(languaje[0])  # elegir una letra
print(languaje[0:8])
print(languaje[3:])
print(languaje[-2])
print(languaje[::-1])
# Funciones (string method)
print(languaje.lower().isupper())
print(languaje.upper())
