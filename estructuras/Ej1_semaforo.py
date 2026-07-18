"""
Ejercicio 4.1 — Semáforo de calificaciones

–	Solicita una nota entre 0 y 100. validar que n sea mayor 0 y menor igual 100
–	Usando if/elif/else clasifica la nota según esta escala:
–	  → 90–100: Excelente   |   75–89: Bueno   |   51–74: Aprobado
–	  → 40–50: Segunda instancia   |   20–39: Reprobado
–	  → 0–19: Abandono
–	Muestra también si el estudiante necesita recuperación (nota < 51).
"""
no_valida = True
while  no_valida :
    nota = float(input("Ingresa tu nota (0-100): "))
    if 0 <= nota <= 100:
        no_valida = False  # Salir del bucle si la nota es válida

        if nota >= 90:
            resultado = "Excelente"
        elif nota >= 75:
            resultado = "Bueno"
        elif nota >= 51:
            resultado = "Aprobado"
        elif nota >= 40:
            resultado = "Segunda instancia"
        elif nota >= 40:
            resultado = "Reprobado"
        else:
            resultado = "Abandono"
        if nota < 51 and nota >= 40:
            necesita_recuperacion = "Si"
        else:
            necesita_recuperacion = "No"
    else:
        print("Error: La nota debe estar entre 0 y 100. Intenta nuevamente.")
print(f"Nota: {nota} → {resultado}")
print(f"Necesita recuperación: {necesita_recuperacion}")
