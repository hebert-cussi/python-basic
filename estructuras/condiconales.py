"""
se tiene que calsicar la nota que ingresa y devolver la clasificacion
si la notas es:
 - mayor o igual 90 mostrar Exelente
 - mayor o igual 75 mostrar Bueno
 - mayor o igual 51 mostrar Aprobado
 - mayor o igual 40 mostrar 2da instacion
 - si es meno a 40 mostar Reprobado
"""

nota = float(input("Nota (0-100): "))
if (nota >0 and nota >100) : cal="La nota debe estar entre 0 y 100"  # V y V se el imprime el valor
elif nota >= 90: cal = "Excelente"
elif nota >= 75: cal = "Bueno"
elif nota >= 51: cal = "Aprobado"
elif nota >= 40: cal = "2da instancia"
else: cal = "Reprobado"
# Se imprime el resultado
print(f"Resultado: {cal}")