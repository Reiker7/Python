class MyEmptyPerson:
    pass


print(MyEmptyPerson)


class Person:
    def __init__(self, name, surname="Moure"):
        self.name = name
        self.surname = surname
        self.last_surname = "ultimo"


my_person = Person("Brais")

print(f"{my_person.name} {my_person.surname} {my_person.last_surname}")

# print(dir(my_person))


class Person2:
    def __init__(self, name, surname, alias="sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # propiedad publica
        self.__name = "name2"  # propiedad privada

    def walk(self):
        print(f"{self.full_name} está caminando")

    def get_name(self):
        return self.__name

    def set_name(self, vaca):
        self.__name = vaca
        return self.__name


my_person = Person2("Brais2", "Moure2")
my_other_person = Person2("Brais3", "Moure3", "alias3")

print(my_person.full_name)
print(type(my_person))
my_person.walk()
print(my_other_person.get_name())
print(my_other_person.set_name("vaca2"))
