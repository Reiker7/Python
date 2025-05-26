my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set))
my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

my_other_set.add("MoureDev")
print(my_other_set)
# Un set es una estructura desordenada, no admite repetidos .
print("Moure" in my_other_set)
print("Mouri" in my_other_set)
my_other_set.remove("Moure")
my_set = list(my_set)
print(type(my_set))
my_new_set = {"Kotlin", "Swift", "Python"}
print(my_new_set)
print(my_other_set.union(my_new_set))
# no admite repetidos aunque lo intentes hacer union del mismo .
print(my_new_set.union(my_new_set).union({"JavaScript", "C#"}))
