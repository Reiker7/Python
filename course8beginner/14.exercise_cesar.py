import string
ALFABETO = string.ascii_lowercase


def alforitmo_cifrado(texto_cifrado, clave):
    """ Esta función descifra el codigo """
    texto_plano = ""
    texto_cifrado = texto_cifrado.lower()
    clave = int(clave)

    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano += letra

        else:
            indice_cifrado = ALFABETO.index(letra)
            texto_plano += ALFABETO[indice_cifrado-clave]

        # print(indice_cifrado)
    print(texto_plano)


texto_final = "Lzav lz bu tluzhql kl wyblihz"


x = range(26)
for n in x:
    if n == 0:
        print("es 0")
    else:
        alforitmo_cifrado(texto_final, n)
