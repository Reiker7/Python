def my_function(primero, segundo="3"):  # puedo poner valores predefinidos
    print(f'{primero} desde función  {str(segundo)}')


my_function("Saludos", )


def print_text(*text):
    print(text)


print_text("Hola", "1", "2", "3")


def print_text(text):
    print(text[1])


print_text(["Hola", "1", "2", "3"])
