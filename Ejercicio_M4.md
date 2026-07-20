# MÓDULO 4 — EJERCICIOS

## Ejercicio 4.1 — Semáforo de calificaciones

- Solicita una nota entre 0 y 100.
- Usando if/elif/else clasifica la nota según esta escala:
  - → 90–100: Excelente   |   75–89: Bueno   |   51–74: Aprobado 
  - → 40–50: Segunda instancia   |   0–39: Reprobado
- Muestra también si el estudiante necesita recuperación (nota < 51).

**Ejercicio resuelto**
```python
# Semáforo de calificaciones
nota = float(input("Ingresa tu nota (0-100): "))

if nota >= 90:
    resultado = "Excelente"
elif nota >= 75:
    resultado = ___________
elif nota >= 51:
    resultado = ___________
elif nota >= 40:
    resultado = ___________
else:
    resultado = ___________

necesita_recuperacion = ___________

print(f"Nota: {nota} → {resultado}")
print(f"Necesita recuperación: {necesita_recuperacion}")
```
## Ejercicio 4.2 — Calculadora de tarifa de taxi	

- Solicita los kilómetros recorridos y el horario (día o noche).
- Calcula la tarifa según estas reglas:
  - → Tarifa base: Bs. 5.00
  - → Km diurno (06:00–22:00): Bs. 2.50 por km
  - → Km nocturno (22:00–06:00): Bs. 3.75 por km (50% adicional)
  - → Descuento del 10% si el recorrido supera 20 km
- Muestra el desglose completo de la tarifa.

**Ejercicio resuelto**
```python
# Calculadora de tarifa de taxi
km       = float(input("Kilómetros recorridos: "))
horario  = input("Horario (dia/noche): ").lower()

tarifa_base = 5.0

if horario == "dia":
    costo_km = km * 2.50
elif horario == "noche":
    costo_km = ___________
else:
    print("Horario inválido")

subtotal = tarifa_base + costo_km

# Aplica descuento si supera 20 km
if km > 20:
    descuento = ___________
else:
    descuento = 0

total = subtotal - descuento

print(f"Tarifa base:  Bs. {tarifa_base:.2f}")
print(f"Costo km:     Bs. {costo_km:.2f}")
print(f"Descuento:    Bs. {descuento:.2f}")
print(f"TOTAL:        Bs. {total:.2f}")
```

## Ejercicio 4.3 — Verificador de año bisiesto

- Solicita un año al usuario.
- Un año es bisiesto si:
  - → Es divisible entre 4 AND (no es divisible entre 100 OR es divisible entre 400).
- Usa el operador % con condicionales para determinarlo.
- Muestra si es bisiesto y cuántos días tiene febrero ese año.

```python
# Verificador de año bisiesto
anio = int(input("Ingresa un año: "))

# Completa la condición:
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or ___________

if es_bisiesto:
    dias_febrero = 29
else:
    dias_febrero = ___________

print('Bisiesto: ' + str(es_bisiesto))
print(f"Febrero tiene {dias_febrero} días.")
```
## Ejercicio 4.4 — Desafío: Cajero automático con menú

- Simula un cajero automático con saldo inicial de Bs. 1000.
- Muestra un menú con 3 opciones: Consultar saldo, Depositar, Retirar.
- Usa if/elif/else para procesar cada opción.
- Valida que el retiro no supere el saldo disponible.
- Muestra mensajes de error apropiados para entradas inválidas.

```python
# Cajero automático
saldo = 1000.0

print("=== CAJERO AUTOMÁTICO ===")
print("1. Consultar saldo")
print("2. Depositar")
print("3. Retirar")
opcion = input("Elige una opción: ")

if opcion == "1":
    print(f"Saldo actual: Bs. {saldo:.2f}")
elif opcion == "2":
    monto = float(input("Monto a depositar: "))
    if monto > 0:
        saldo += ___________
        print(f"Depósito exitoso. Nuevo saldo: Bs. {saldo:.2f}")
    else:
        print("Monto inválido.")
elif opcion == "3":
    monto = float(input("Monto a retirar: "))
    if monto <= 0:
        print("Monto inválido.")
    elif monto > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= ___________
        print(f"Retiro exitoso. Nuevo saldo: Bs. {saldo:.2f}")
else:
    print("Opción no válida.")
```

## Ejercicio 4.5 — Contador con while

- Usa un bucle while para imprimir los números del 1 al 20.
- En la misma línea, muestra si cada número es par o impar.
- Al final muestra la suma total de todos los números.

```python
# Contador con while
numero     = 1
suma_total = 0

while numero <= 20:
    paridad = ___________
    print(f"{numero:>2} → {paridad}")
    suma_total += numero
    numero += ___________

print(f"Suma total 1–20: {suma_total}")
```

## Ejercicio 4.6 — Validador de contraseña

- Simula un sistema de login con máximo 3 intentos.
- La contraseña correcta es 'python2024'.
- Usa un bucle while para pedir la contraseña.
- Muestra cuántos intentos quedan en cada vuelta.
- Bloquea el acceso si se agotan los 3 intentos.

```python
# Validador de contraseña con intentos
contrasena_correcta = "python2024"
max_intentos = 3
intentos     = 0
acceso       = False

while intentos < max_intentos:
    clave = input(f"Contraseña ({max_intentos - intentos} intento(s) restantes): ")
    intentos += 1

    if clave == contrasena_correcta:
        acceso = ___________
        break
    else:
        print("Contraseña incorrecta.")

if acceso:
    print("Acceso concedido. ¡Bienvenido!")
else:
    print("Acceso bloqueado. Demasiados intentos fallidos.")
```
## Ejercicio 4.7 — Desafío: Adivina el número

- Genera un número secreto entre 1 y 50 (usa el valor 37 para pruebas).
- El usuario tiene máximo 7 intentos para adivinarlo.
- Da pistas: 'muy frío' (diferencia > 20), 'frío' (10–20), 'tibio' (5–9), 'caliente' (< 5).
- Muestra el número de intentos usados al final.
- Usa break para salir cuando acierte.

```python
# Adivina el número con pistas
secreto    = 37
max_intent = 7
intento    = 0
acertado   = False

print("Adivina el número entre 1 y 50")

while intento < max_intent and not acertado:
    intento += 1
    guess = int(input(f"Intento {intento}/{max_intent}: "))
    diferencia = abs(guess - secreto)

    if guess == secreto:
        acertado = True
        break
    elif diferencia > 20:
        pista = "❄️  Muy frío"
    elif diferencia > 10:
        pista = ___________
    elif diferencia > 5:
        pista = ___________
    else:
        pista = "🔥 Caliente"

    print(f"{pista}. {"Más alto" if guess < secreto else "Más bajo"}.")

if acertado:
    print(f"¡Correcto! Lo lograste en {intento} intento(s).")
else:
    print(f"¡Se acabaron los intentos! El número era {secreto}.")
```

## Ejercicio 4.8 — Tablas de multiplicar con for

- Solicita un número al usuario.
- Genera su tabla de multiplicar del 1 al 12 usando un bucle for.
- Usa range() con los parámetros correctos.
- Resalta con un símbolo ★ los resultados que sean múltiplos de 10.
- Al final muestra la suma de todos los resultados de la tabla.
```python
# Tabla de multiplicar
num = int(input("Ingresa un número para su tabla: "))
suma = 0

print(f"\n=== TABLA DEL {num} ===")
for i in range(___, ___):
    resultado = num * i
    suma     += resultado
    marca     = " ★" if resultado % 10 == 0 else ""
    print(f"{num} x {i:>2} = {resultado:>4}{marca}")

print(f"Suma total: {suma}")
```
## Ejercicio 4.9 — Patrón de figuras con bucles anidados
- Solicita un número N al usuario (entre 1 y 9).
- Genera los siguientes 3 patrones con bucles anidados:
  - → Cuadrado de N×N con asteriscos
  - → Triángulo creciente (fila i tiene i asteriscos)
  - → Triángulo decreciente (fila i tiene N-i+1 asteriscos)
- Separa cada patrón con una línea en blanco.

```python
# Patrones con bucles anidados
N = int(input("Ingresa N (1-9): "))

# Patrón 1: Cuadrado N×N
print(f"Cuadrado {N}x{N}:")
for fila in range(N):
    for col in range(___):
        print("*", end="")
    print()

# Patrón 2: Triángulo creciente
print("\nTriángulo creciente:")
for fila in range(1, N+1):
    for col in range(___):
        print("*", end="")
    print()

# Patrón 3: Triángulo decreciente
print("\nTriángulo decreciente:")
for fila in range(N, 0, -1):
    for col in range(___):
        print("*", end="")
    print()
```
## Ejercicio 4.10 — Desafío: Sistema de calificaciones grupal

- Usando un bucle while, solicita las notas de N estudiantes (N lo define el usuario).
- Para cada estudiante pide nombre y nota.
- Clasifica la nota con if/elif/else (Excelente/Bueno/Aprobado/Reprobado).
- Usa continue para ignorar notas inválidas (< 0 o > 100).
- Al terminar muestra: promedio del grupo, nota más alta, nota más baja, total aprobados y reprobados.
```python
# Sistema de calificaciones grupal
n = int(input("¿Cuántos estudiantes? "))
i          = 0
suma       = 0
nota_max   = 0
nota_min   = 100
aprobados  = 0
reprobados = 0

while i < n:
    nombre = input(f"\nNombre estudiante {i+1}: ")
    nota   = float(input(f"Nota de {nombre}: "))

    if nota < 0 or nota > 100:
        print("Nota inválida. Se omite.")
        continue

    i += 1
    suma += nota

    if nota > nota_max:  nota_max = nota
    if nota < nota_min:  nota_min = nota

    if nota >= 51:
        aprobados  += ___________
        estado = "Aprobado"
    else:
        reprobados += ___________
        estado = "Reprobado"

    print(f"  → {estado}")

print("\n=== RESUMEN GRUPAL ===")
print(f"Promedio:   {suma/n:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")
print(f"Aprobados:  {aprobados}/{n}")
print(f"Reprobados: {reprobados}/{n}")
```
 