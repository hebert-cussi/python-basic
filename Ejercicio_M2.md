# MÓDULO 2 — EJERCICIOS

## Ejercicio 2.1 — Mi tarjeta de presentación	Fácil

 - Declara variables con tu información personal y muéstralas de forma ordenada
 - Usa al menos: una variable str, una int, una float y una bool
 - Muestra el tipo de cada variable con type()
 
**Ejercicio resuelto**
```python
# Tarjeta de presentación

nombre = "___________"    # str
edad = ___________        # int
altura = ___________      # float
tiene_mascota = ___________  # bool

print('=== MI TARJETA ===')
print('Nombre:', nombre, '| Tipo:', type(nombre))
print('Edad:', edad, '| Tipo:', type(edad))
print('Altura:', altura, '| Tipo:', type(altura))
print('Tiene mascota:', tiene_mascota, '| Tipo:', type(tiene_mascota))
```
## Ejercicio 2.2 — Calculadora de edad	Fácil

- Solicita al usuario su nombre y año de nacimiento con input()
- Calcula su edad actual (usa 2024 como año actual)
- Calcula cuántos años tendrá en el año 2050
- Muestra todos los resultados con un mensaje claro

**Ejercicio resuelto**
```python
# Calculadora de edad
nombre = input("¿Cuál es tu nombre? ")
anio_nac = int(input("¿En qué año naciste? "))

# Completa los cálculos:
edad_actual = ___________
edad_2050 = ___________

print('Hola,', nombre)
print('Actualmente tienes', edad_actual, 'años')
print('En 2050 tendrás', edad_2050, 'años')
```
## Ejercicio 2.3 — Conversor de temperatura	Medio

- Solicita una temperatura en grados Celsius al usuario
- Conviértela a Fahrenheit usando la fórmula: F = (C × 9/5) + 32
- Conviértela también a Kelvin: K = C + 273.15
- Muestra los resultados con 2 decimales usando round()

**Ejercicio resuelto**
```python
# Conversor de temperatura
celsius = float(input("Ingresa la temperatura en °C: "))

# Aplica las fórmulas:
fahrenheit = ___________
kelvin = ___________

print('=== RESULTADO ===')
print(celsius, '°C =', round(fahrenheit, 2), '°F')
print(celsius, '°C =', round(kelvin, 2), 'K')
```
## Ejercicio 2.4 — Calculadora de descuento	Medio

- Solicita el nombre del producto, precio original y porcentaje de descuento
- Calcula el monto del descuento y el precio final
- Muestra un recibo formateado con todos los datos

Como resultado deberia de mostrar:
```python
====== RECIBO ======
Producto: 
Precio original: Bs. 
Descuento (valor_descuento %): Bs. 
PRECIO FINAL: Bs.
===================
```

## Ejercicio 2.5 — Desafío: Detectar tipos sin type()

- El usuario ingresa 3 valores. Tu programa debe clasificarlos SIN usar type().
- Usa solo las funciones int(), float(), str() e isdigit() para determinar el tipo.
- **Pista:** Si int(valor) no lanza error → es entero. Si float(valor) no lanza error → es decimal.

Ayuda:
   - usar la funcion isdigit() y la funcion de comparacion if

## Ejercicio 2.6 — Intercambio de variables	Fácil

- Declara dos variables: a = 10 y b = 25.
- Intercambia sus valores usando una variable temporal auxiliar.
- Luego hazlo de nuevo usando el método de desempaquetado de Python (en una sola línea).
- Muestra los valores antes y después de cada intercambio con type() para verificar.

```python
# Intercambio de variables
a = 10
b = 25
print(f"Antes:  a = {a}, b = {b}")

# Método 1: usando variable temporal
temp = ___________
a    = ___________
b    = ___________
print(f"Después (método 1): a = {a}, b = {b}")

# Reinicia valores
a, b = 10, 25

# Método 2: desempaquetado Python (una sola línea)
___________ = ___________
print(f"Después (método 2): a = {a}, b = {b}")
```
## Ejercicio 2.7 — Operaciones con strings	Fácil

- Solicita el nombre completo del usuario (nombre y apellido juntos).
- Usando solo métodos de string, obtén y muestra:
  - → El nombre en MAYÚSCULAS
  - → El nombre en minúsculas
  - → La cantidad de caracteres (incluye espacios)
  - → Las primeras 3 letras del nombre
  - → El nombre al revés
  - → Si contiene la letra 'a' (True/False)
```python
# Operaciones con strings
nombre = input("Ingresa tu nombre completo: ")

# Completa usando métodos de string:
en_mayusculas  = ___________
en_minusculas  = ___________
num_caracteres = ___________
primeras_3     = ___________
al_reves       = ___________
tiene_a        = ___________

print(f"Original:     {nombre}")
print(f"Mayúsculas:   {en_mayusculas}")
print(f"Minúsculas:   {en_minusculas}")
print(f"Caracteres:   {num_caracteres}")
print(f"Primeras 3:   {primeras_3}")
print(f"Al revés:     {al_reves}")
print(f"Tiene 'a':    {tiene_a}")
```
## Ejercicio 2.8 — Conversor de monedas múltiple	Medio

- Solicita un monto en bolivianos (Bs.).
- Conviértelo a: dólares americanos, euros y pesos chilenos.
- Usa las siguientes tasas de cambio aproximadas:
  - → 1 USD = 6.96 Bs.   |   1 EUR = 7.55 Bs.   |   1 CLP = 0.0076 Bs.
- Convierte cada monto declarando una variable float para la tasa.
- Muestra los resultados con 2 decimales y el símbolo de cada moneda.
```python
# Conversor de monedas — Bolivia
bolivianos = float(input("Monto en bolivianos (Bs.): "))

# Tasas de cambio (Bs. por unidad extranjera)
tasa_usd = 6.96
tasa_eur = 7.55
tasa_clp = 0.0076

# Calcula las conversiones:
dolares = ___________
euros   = ___________
pesos   = ___________

print(f"\nBs. {bolivianos:.2f} equivale a:")
print(f"  $ {dolares:.2f} USD")
print(f"  € {euros:.2f} EUR")
print(f"  $ {pesos:,.0f} CLP")
```

## Ejercicio 2.9 — Calculadora de IMC	Medio

–	Solicita el nombre, peso en kg y altura en metros del usuario.
–	Calcula el Índice de Masa Corporal: IMC = peso / (altura ** 2).
–	Convierte los valores de entrada al tipo correcto (float).
–	Clasifica el resultado según la OMS:
–	  → IMC < 18.5: Bajo peso   |   18.5–24.9: Normal
–	  → 25.0–29.9: Sobrepeso    |   >= 30: Obesidad
–	Muestra el IMC con 1 decimal y la clasificación.
```python
# Calculadora de IMC
nombre = input("Nombre: ")
peso   = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Calcula el IMC:
imc = ___________

# Clasificación (completa las condiciones):
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < ___________:
    clasificacion = "Normal"
elif imc < ___________:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"\n=== IMC de {nombre} ===")
print(f"Peso: {peso} kg | Altura: {altura} m")
print(f"IMC: {imc:.1f}")
print(f"Clasificación: {clasificacion}")
```

## Ejercicio 2.10 — Desafío: Calculadora de propina inteligente	Desafío

- Solicita: nombre del restaurante, monto de la cuenta y número de comensales.
- Calcula la propina según el monto total:
  - → Cuenta < Bs. 100: propina 10%
  - → Cuenta entre Bs. 100 y 300: propina 12%
  - → Cuenta > Bs. 300: propina 15%
- Calcula cuánto debe pagar cada comensal (cuenta + propina / número de personas).
- Convierte todos los inputs al tipo correcto antes de operar.
- Muestra un resumen completo con todos los datos y 2 decimales.

```python
# Calculadora de propina — Desafío
restaurante  = input("Nombre del restaurante: ")
cuenta       = float(input("Monto de la cuenta (Bs.): "))
comensales   = int(input("Número de comensales: "))

# Determina el porcentaje de propina:
if cuenta < 100:
    pct_propina = ___________
elif cuenta <= 300:
    pct_propina = ___________
else:
    pct_propina = ___________

# Calcula los montos:
propina      = cuenta * pct_propina
total        = ___________
por_persona  = ___________

sep = "=" * 38
print(sep)
print(f"  {restaurante.upper()}")
print("-" * 38)
print(f"  Cuenta:        Bs. {cuenta:>8,.2f}")
print(f"  Propina ({pct_propina*100:.0f}%): Bs. {propina:>8,.2f}")
print(f"  Total:         Bs. {total:>8,.2f}")
print("-" * 38)
print(f"  Por persona ({comensales}): Bs. {por_persona:>6,.2f}")
print(sep)
```