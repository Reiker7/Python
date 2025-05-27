### Conditionals ###

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True
    print("se ejecuta la condición del if")
else:
    print("El valor es False")

my_condition = 5 * 2

if my_condition == 10:
    print("se ejecuta la condición del segundo if")
if my_condition:  # al ser true vuelve a entrar
    print(bool(my_condition))
    print("se ejecuta la condición del tercer if")
# my_condition = 11 si lo cambiara entrar por el elif
if my_condition >= 10 and my_condition >= 20:
    print("se ejecuta la condición del cuarto if")
elif my_condition == 11:
    print("es 11")
else:
    print("no se cumple el cuarto")
    print("no se cumple el cuarto")  # tabulado lo considera dentro del else

my_condition = 0  # ahora 0 es false
if not my_condition:
    print("5")  # no entraria por el if pero le añadí not

print("La ejecución continúa")
