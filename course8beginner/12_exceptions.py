### Excetion Handling ###

numberOne = 5
numberTwo = "1"

try:
    print(numberOne + numberTwo)
except ValueError:
    print("ErrorValue")
except TypeError as e:
    print(f"TypeError revisa: {e}")
except:
    print("Something else went wrong")
else:  # Opcional
    print("saludos")
finally:  # Opcional - se ejecuta siempre
    print("final")

### Excetion por tipo ###
