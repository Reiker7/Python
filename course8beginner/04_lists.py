### Lists ###
my_list = list()  # lista
print(type(my_list))
my_otherlist = []  # lista(array)
print(len(my_list))

my_list = [32, 40, 17, 24, 30, 30]
print(my_list)
print(len(my_list))

my_otherlist = [35, 1.77, "Brais", 'Moure']
print(my_otherlist)
print(type(my_otherlist))

print(my_otherlist[0])
print(my_otherlist[-1])
print(my_list.count(30))  # cuenta los mismo que le pasamos

age, height, name, surname = my_otherlist  # Desempaquetar
print(name)
print(my_list + my_otherlist)  # Concatenar listas
# Desempaquetar puede ser foco errores
age, height, name, surname = my_otherlist[1], my_otherlist[2], my_otherlist[0], my_otherlist[3]
print(age)

my_otherlist.append("Final")  # añadir al final
my_otherlist.insert(1, "insertPosi")  # insertar posición
my_otherlist.remove(35)  # Remueve elemento conocido
print(my_otherlist)
del my_otherlist[1]  # Remueve por indice
cut_save = my_otherlist.pop(1)  # eliminar elemento,  puede guardarse
print(my_otherlist)
print(cut_save)
my_new_list = my_otherlist.copy()  # Copia en este punto
my_otherlist.clear()  # Elimina todo
print(my_otherlist)
print(my_new_list)
my_new_list.reverse()
print(my_new_list)
# .sort() ordena en forma creciente
print(my_new_list[1:2])
