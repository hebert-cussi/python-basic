# MÓDULO 3 — EJERCICIOS

## Ejercicio 3.1 — Calculadora de operaciones básicas	

-	Solicita dos números al usuario.
-	Calcula y muestra: suma, resta, multiplicación, división, división entera, módulo y potencia.
-	Usa f-strings para mostrar cada resultado en una línea separada con formato claro.

**Ejercicio resuelto**
```python
# Calculadora básica — completa las operaciones
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print(f"Suma:            {a} + {b} = {___________}")
print(f"Resta:           {a} - {b} = {___________}")
print(f"Multiplicación:  {a} * {b} = {___________}")
print(f"División:        {a} / {b} = {___________:.2f}")
print(f"División entera: {a} // {b} = {___________}")
print(f"Módulo:          {a} % {b} = {___________}")
print(f"Potencia:        {a} ** {b} = {___________}")
```
## Ejercicio 3.2 — Verificador de condiciones	Fácil

- Solicita la edad y el saldo en cuenta del usuario.
- Usa operadores de comparación y lógicos para determinar:
  - → ¿Es mayor de edad? (>= 18)
  - → ¿Tiene saldo suficiente para comprar algo de Bs. 200?
  - → ¿Puede hacer la compra? (mayor de edad AND saldo >= 200)
  - → ¿Necesita ayuda? (menor de edad OR sin saldo suficiente)
**Ejercicio resuelto**
```python
# Verificador de condiciones
edad  = int(input("Tu edad: "))
saldo = float(input("Tu saldo (Bs.): "))

# Completa las expresiones lógicas:
es_mayor       = ___________
saldo_ok       = ___________
puede_comprar  = ___________
necesita_ayuda = ___________

print(f"Es mayor de edad:         {es_mayor}")
print(f"Saldo suficiente (>=200): {saldo_ok}")
print(f"Puede comprar:            {puede_comprar}")
print(f"Necesita ayuda:           {necesita_ayuda}")
**Ejercicio resuelto**
```
## Ejercicio 3.3 — Conversor de unidades múltiple	

-	Solicita una distancia en kilómetros.
-	Conviértela a: metros, centímetros, millas y pies.
-	Usa operadores aritméticos para cada conversión.
-	Muestra los resultados con f-strings y 2 decimales.
```python
# Conversor de distancias
km = float(input("Distancia en kilómetros: "))

# Factores: 1 km = 1000 m = 100000 cm = 0.621371 mi = 3280.84 ft
metros      = km * ___________
centimetros = km * ___________
millas      = km * ___________
pies        = km * ___________

print(f"{km} km equivale a:")
print(f"  {metros:,.0f} metros")
print(f"  {centimetros:,.0f} centímetros")
print(f"  {millas:.4f} millas")
print(f"  {pies:,.2f} pies")
```
## Ejercicio 3.4 — Tabla de precedencia en práctica	Medio

-	Sin ejecutar el código, predice el resultado de cada expresión.
-	Luego escribe el código y verifica tus predicciones.
-	Explica con un comentario por qué Python llega a ese resultado.
```python
# Predice el resultado ANTES de ejecutar:
expr1 = 2 + 3 * 4           # Tu predicción: ___
expr2 = (2 + 3) * 4         # Tu predicción: ___
expr3 = 10 - 2 ** 3         # Tu predicción: ___
expr4 = 15 // 4 + 3         # Tu predicción: ___
expr5 = 15 // (4 + 3)       # Tu predicción: ___
expr6 = 2 ** 3 ** 2         # Tu predicción: ___ (cuidado!)
expr7 = not 5 > 3 and 2 < 4 # Tu predicción: ___

print(expr1, expr2, expr3, expr4, expr5, expr6, expr7)

# Explica cada resultado:
# expr1: ___
# expr3: ___
# expr7: ___
```
## Ejercicio 3.5 — Desafío: Mini sistema de calificaciones	Desafío

-	Solicita el nombre del estudiante y sus 4 notas del semestre.
-	Calcula el promedio usando operadores aritméticos y asignación compuesta.
-	Determina si aprobó (promedio >= 51) y si tiene derecho a segunda instancia (40 <= promedio < 51).
-	Calcula cuántos puntos le faltan o sobran para aprobar.
-	Genera un reporte completo usando f-strings con formato profesional.
```python
# Sistema de calificaciones
nombre = input("Nombre del estudiante: ")
n1 = float(input("Nota 1 (sobre 100): "))
n2 = float(input("Nota 2 (sobre 100): "))
n3 = float(input("Nota 3 (sobre 100): "))
n4 = float(input("Nota 4 (sobre 100): "))

total = n1
total += ___   
total += ___   
total += ___   
promedio = total / 4

aprobado          = promedio >= 51
segunda_instancia = ___ and ___
diferencia        = promedio - 51

sep = "-" * 40
print(sep)
print(f"  REPORTE: {nombre.upper()}")
print(f"  Notas: {n1:.1f} | {n2:.1f} | {n3:.1f} | {n4:.1f}")
print(f"  Promedio:       {promedio:.2f} / 100")
print(f"  Aprobado:       {aprobado}")
print(f"  2da instancia:  {segunda_instancia}")
print(f"  Diferencia:     {diferencia:+.2f} pts")
print(sep)
```

# Ejercicio 3.6 — Detector de números pares e impares con módulo	Fácil

-	Solicita 3 números enteros al usuario.
-	Para cada número usa el operador % para determinar si es par o impar.
-	Muestra también el resto de dividir cada número entre 3.
-	Usa f-strings para presentar los resultados en formato tabla.
```python
# Detector par/impar con módulo
a = int(input("Primer número:  "))
b = int(input("Segundo número: "))
c = int(input("Tercer número:  "))

# Completa usando el operador %
a_es_par    = a % 2 == ___
b_es_par    = ___
c_es_par    = ___

a_resto_3   = a % 3
b_resto_3   = ___
c_resto_3   = ___

print(f"Número  Par/Impar  Resto entre 3")
print(f"{a:>6}  {"Par" if a_es_par else "Impar":>9}  {a_resto_3}")
print(f"{b:>6}  {"Par" if b_es_par else "Impar":>9}  {b_resto_3}")
print(f"{c:>6}  {"Par" if c_es_par else "Impar":>9}  {c_resto_3}")
```

## Ejercicio 3.7 — Calculadora de IVA y precios	Fácil

-	Solicita el nombre de un producto y su precio sin IVA.
-	Calcula el IVA (13% según Bolivia) usando operadores aritméticos.
-	Calcula también el precio con descuento del 10% sobre el precio final.
-	Usa operadores de asignación compuesta para aplicar el descuento.
-	Determina con operadores lógicos si el precio final es 'accesible' (< Bs. 500).
```python
# Calculadora de IVA — Bolivia 13%
producto = input("Nombre del producto: ")
precio_neto = float(input("Precio sin IVA (Bs.): "))

# Calcula IVA y precio con IVA
iva          = precio_neto * ___________
precio_total = precio_neto + iva

# Aplica descuento del 10% con asignación compuesta
precio_desc = precio_total
precio_desc *= ___________      # descuento del 10%

# Verifica accesibilidad
es_accesible = precio_total < 500 and precio_neto > 0

print(f"\n=== {producto.upper()} ===")
print(f"Precio neto:      Bs. {precio_neto:,.2f}")
print(f"IVA (13%):        Bs. {iva:,.2f}")
print(f"Precio con IVA:   Bs. {precio_total:,.2f}")
print(f"Con descuento 10%: Bs. {precio_desc:,.2f}")
print(f"Precio accesible: {es_accesible}")
```
## Ejercicio 3.8 — Analizador de temperatura corporal	Medio

- Solicita la temperatura corporal del usuario en °C.
- Usa operadores de comparación y lógicos para clasificarla:
  - → Hipotermia: < 36.0°C
  - → Normal: >= 36.0 y <= 37.5°C
  - → Febrícula: > 37.5 y <= 38.5°C
  - → Fiebre: > 38.5°C
-	Calcula la diferencia respecto a la temperatura normal (37.0°C).
-	Formatea la salida con f-strings mostrando la temperatura con 1 decimal.
```python
# Analizador de temperatura corporal
temp = float(input("Temperatura corporal (°C): "))

# Clasificación con operadores lógicos
hipotermia = temp < 36.0
normal     = temp >= 36.0 and temp <= 37.5
febricula  = ___________ and ___________
fiebre     = ___________

# Diferencia respecto a temperatura normal
diferencia = temp - 37.0

# Determinar diagnóstico
if hipotermia:
    diagnostico = "HIPOTERMIA"
elif normal:
    diagnostico = "NORMAL"
elif febricula:
    diagnostico = "FEBRÍCULA"
else:
    diagnostico = "FIEBRE"

print(f"Temperatura: {temp:.1f}°C")
print(f"Diagnóstico: {diagnostico}")
print(f"Diferencia:  {diferencia:+.1f}°C respecto a 37.0°C")
```
## Ejercicio 3.9 — Generador de tabla de multiplicar con formato	Medio

- Solicita un número entero al usuario.
- Genera su tabla de multiplicar del 1 al 12 usando operadores aritméticos.
- Usa el operador de asignación compuesta para acumular el resultado.
- Formatea la salida con f-strings alineando los números a la derecha.
- Al final muestra la suma total de todos los resultados de la tabla.

```python
# Tabla de multiplicar con formato
num = int(input("Ingresa un número: "))

suma_total = 0
print(f"\n=== TABLA DEL {num} ===")
print("-" * 22)

# Completa: genera los 12 resultados
for i in range(1, 13):
    resultado = num * i
    suma_total += ___________
    print(f"{num:>3} x {i:>2} = {resultado:>4}")

print("-" * 22)
print(f"Suma total: {suma_total}")
```

## Ejercicio 3.10 — Desafío: Simulador de caja registradora	Desafío

- Simula una caja registradora que procesa 3 productos.
- Para cada producto solicita: nombre, precio unitario y cantidad.
- Calcula subtotal de cada producto con operadores aritméticos.
- Usa operadores de asignación compuesta para acumular el total.
- Aplica descuento del 15% si el total supera Bs. 500 (operadores de comparación y lógicos).
- Aplica IVA del 13% sobre el monto neto después del descuento.
- Genera un ticket de compra completo con f-strings y formato profesional.
```python
# Caja registradora — 3 productos
print("=== INGRESO DE PRODUCTOS ===")

# Producto 1
p1 = input("Producto 1 — Nombre: ")
pr1 = float(input("Producto 1 — Precio (Bs.): "))
c1  = int(input("Producto 1 — Cantidad: "))
sub1 = pr1 * c1

# Producto 2 y 3 — repite el patrón
# ...

# Acumula el total
total = 0
total += ___
total += ___
total += ___

# Descuento si total > 500
aplica_desc = ___________
descuento   = total * 0.15 if aplica_desc else 0
base        = total - descuento
iva         = base * 0.13
total_final = base + iva

# Ticket de compra
sep = "=" * 38
print(sep)
print(f"  TICKET DE COMPRA")
print("-" * 38)
print(f"  {p1:<20} Bs. {sub1:>7,.2f}")
# ... imprime p2 y p3
print("-" * 38)
print(f"  Subtotal:          Bs. {total:>7,.2f}")
print(f"  Descuento 15%:     Bs. {descuento:>7,.2f}")
print(f"  IVA 13%:           Bs. {iva:>7,.2f}")
print(sep)
print(f"  TOTAL A PAGAR:     Bs. {total_final:>7,.2f}")
print(sep)
```