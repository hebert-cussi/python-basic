"""
intente adivinar el numero numero secreto
"""
secreto = 42
adivinado = False
while not adivinado:
    intento = int(input("Adivina (1-100): "))
    if intento == secreto: adivinado = True
    elif intento < secreto: print("Más alto")
    else: print("Más bajo")
print("¡Correcto!")
