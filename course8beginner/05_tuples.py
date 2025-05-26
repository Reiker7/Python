my_tuple = tuple()
my_other_tuple = ()
my_tuple = (35, 1.77, "Brais", "Mouse", "Brais")
print(type(my_tuple))
print(my_tuple)
print(my_tuple[2])
print(my_tuple.count("Brais"))
print(my_tuple.index(35))

# tupla es inmutable
my_other_tuple = my_tuple + my_tuple
print(my_other_tuple)

del my_tuple  # aun siendo inmutable puede borrarse
