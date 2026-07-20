# MÓDULO 5 — EJERCICIOS

## Ejercicio 5.1 — Mi primera función — Saludo personalizado

- Define una función llamada saludar que reciba nombre y ciudad como parámetros.
- La función debe imprimir un mensaje personalizado de bienvenida.
- Llama a la función al menos 3 veces con diferentes datos.
- Agrega un docstring describiendo qué hace la función.

```python
# Define la función con su docstring
def saludar(nombre, ciudad):
    """
    ___________
    """
    ___________

# Llama a la función 3 veces:
saludar("Ana",    "La Paz")
saludar("Carlos", "Cochabamba")
saludar("María",  "Santa Cruz")
```

## Ejercicio 5.2 — Funciones matemáticas básicas

- Crea 4 funciones: area_rectangulo, area_circulo, perimetro_rectangulo, perimetro_circulo.
- Cada función debe recibir los parámetros necesarios y RETORNAR el resultado (no imprimir).
- Llama a cada función y muestra los resultados con f-strings y 2 decimales.

```python
# Usa PI = 3.14159
PI = 3.14159

def area_rectangulo(base, altura):
    """Retorna el área de un rectángulo."""
    return ___________

def area_circulo(radio):
    """Retorna el área de un círculo."""
    return ___________

def perimetro_rectangulo(base, altura):
    return ___________

def perimetro_circulo(radio):
    return ___________

# Llama y muestra resultados:
print(f"Área rectángulo (4x6):   {area_rectangulo(4, 6):.2f}")
print(f"Área círculo (r=5):      {area_circulo(5):.2f}")
print(f"Perímetro rect. (4x6):  {perimetro_rectangulo(4, 6):.2f}")
print(f"Perímetro círculo (r=5): {perimetro_circulo(5):.2f}")
```
## Ejercicio 5.3 — Calculadora de factura con funciones

- Crea 3 funciones separadas: calcular_subtotal, aplicar_descuento, calcular_iva.
- calcular_subtotal(precio, cantidad) → retorna precio * cantidad.
- aplicar_descuento(subtotal, pct) → retorna (monto_descontado, descuento). Valor por defecto pct=0.
- calcular_iva(base, tasa=0.13) → retorna el IVA sobre la base.
- Usa las 3 funciones en un programa principal que genere una factura completa.

```python
def calcular_subtotal(precio, cantidad):
    """Retorna precio * cantidad."""
    return ___________

def aplicar_descuento(subtotal, pct=0):
    """Retorna (total_con_desc, monto_descuento)."""
    descuento = subtotal * (pct / 100)
    return ___________, ___________

def calcular_iva(base, tasa=0.13):
    """Retorna el IVA sobre la base imponible."""
    return ___________

# Programa principal:
producto  = input("Producto: ")
precio    = float(input("Precio: "))
cantidad  = int(input("Cantidad: "))
desc_pct  = float(input("Descuento %: "))

subtotal          = calcular_subtotal(precio, cantidad)
base, monto_desc  = aplicar_descuento(subtotal, desc_pct)
iva               = calcular_iva(base)
total             = base + iva

print(f"Subtotal: Bs. {subtotal:.2f}")
print(f"Desc.:    Bs. {monto_desc:.2f}")
print(f"IVA 13%:  Bs. {iva:.2f}")
print(f"TOTAL:    Bs. {total:.2f}")
```

## Ejercicio 5.4 — Desafío: Sistema de calificaciones con funciones

- Crea una función obtener_clasificacion(nota) que retorne el texto de la calificación.
- Crea una función calcular_promedio(notas) que reciba una lista y retorne el promedio.
- Crea una función generar_reporte(nombre, notas) que use las dos anteriores e imprima el reporte.
- La función generar_reporte debe también retornar True si aprobó (promedio >= 51) o False si no.
- Llama a generar_reporte para al menos 3 estudiantes diferentes.

```python
def obtener_clasificacion(nota):
    """Retorna la clasificación según la nota."""
    if nota >= 90:   return ___________
    elif nota >= 75: return ___________
    elif nota >= 51: return ___________
    elif nota >= 40: return ___________
    else:            return ___________

def calcular_promedio(notas):
    """Retorna el promedio de una lista de notas."""
    return ___________

def generar_reporte(nombre, notas):
    """Imprime el reporte del estudiante y retorna True si aprobó."""
    promedio  = calcular_promedio(notas)
    clasif    = obtener_clasificacion(promedio)
    aprobado  = promedio >= 51
    sep = "-" * 35
    print(sep)
    print(f"  Estudiante: {nombre}")
    print(f"  Notas: {notas}")
    print(f"  Promedio: {promedio:.1f} — {clasif}")
    print(f"  Estado: {"Aprobado" if aprobado else "Reprobado"}")
    print(sep)
    return aprobado

# Llama para 3 estudiantes:
generar_reporte("Ana López",    [85, 92, 78, 88])
generar_reporte("Carlos Ramos", [45, 52, 38, 41])
generar_reporte("María Quispe", [95, 88, 92, 97])
```

## Ejercicio 5.5 — Explorador de scope

- Crea una variable global llamada ciudad = 'La Paz'.
- Crea una función ver_scope() que tenga una variable local pais = 'Bolivia' y muestre ambas.
- Crea una función modificar_ciudad() que use global para cambiar la variable ciudad.
- Llama a las funciones en orden y observa cómo cambia ciudad.

```python
# Variable global
ciudad = "La Paz"

def ver_scope():
    pais = "Bolivia"   # variable local
    print(f"Dentro de ver_scope:")
    print(f"  ciudad (global): {ciudad}")
    print(f"  pais   (local):  {pais}")

def modificar_ciudad(nueva_ciudad):
    global ciudad
    ciudad = ___________
    print(f"Ciudad modificada a: {ciudad}")

ver_scope()
modificar_ciudad("Cochabamba")
ver_scope()
print(f"ciudad desde el main: {ciudad}")
```

## Ejercicio 5.6 — Usando funciones incorporadas

- Crea una lista de 8 números: [15, 3, 42, 7, 88, 23, 61, 9].
- Sin usar bucles ni definir funciones propias, usa SOLO funciones incorporadas para obtener:
  -   → El total (sum), el máximo (max), el mínimo (min), la cantidad (len).
  -   → El promedio calculado con sum y len.
  -   → La lista ordenada de menor a mayor y de mayor a menor (sorted).
  -   → El valor absoluto de la diferencia entre max y min (abs).

```python
numeros = [15, 3, 42, 7, 88, 23, 61, 9]

total       = ___________
maximo      = ___________
minimo      = ___________
cantidad    = ___________
promedio    = ___________
ascendente  = ___________
descendente = sorted(numeros, reverse=___________)
rango       = ___________

print(f"Lista:       {numeros}")
print(f"Total:       {total}")
print(f"Máximo:      {maximo}")
print(f"Mínimo:      {minimo}")
print(f"Cantidad:    {cantidad}")
print(f"Promedio:    {promedio:.2f}")
print(f"Ascendente:  {ascendente}")
print(f"Descendente: {descendente}")
print(f"Rango:       {rango}")
```
## Ejercicio 5.7 — Validador de datos con funciones	Medio

- Crea las siguientes funciones de validación, cada una retorna True o False:
  -   → es_positivo(num): retorna True si num > 0.
  -   → es_entero_str(texto): retorna True si el texto representa un número entero.
  -   → longitud_valida(texto, min_len=3, max_len=20): retorna True si la longitud está en rango.
  -   → es_email_valido(email): retorna True si contiene '@' y '.' después del '@'.
- Crea una función validar_registro(nombre, edad_str, email) que use las 4 anteriores y retorne un dict con los resultados.
```python
def es_positivo(num):
    return ___________

def es_entero_str(texto):
    return ___________

def longitud_valida(texto, min_len=3, max_len=20):
    return min_len <= len(texto) <= max_len

def es_email_valido(email):
    tiene_arroba = '@' in email
    if not tiene_arroba: return False
    partes = email.split('@')
    return '.' in partes[1]

def validar_registro(nombre, edad_str, email):
    return {
        "nombre_ok": longitud_valida(nombre),
        "edad_ok":   es_entero_str(edad_str) and es_positivo(int(edad_str) if es_entero_str(edad_str) else -1),
        "email_ok":  es_email_valido(email),
    }

resultado = validar_registro("Ana", "25", "ana@gmail.com")
print(resultado)
resultado2 = validar_registro("X", "abc", "sinrroba.com")
print(resultado2)
```

## Ejercicio 5.8 — Funciones con múltiples retornos

- Crea una función analizar_texto(texto) que retorne 5 valores:
  -   → Número de caracteres totales (con espacios).
  -   → Número de palabras.
  -   → Número de vocales.
  -   → El texto en mayúsculas.
  -   → La primera y última palabra.
- Muestra todos los resultados con f-strings.

```python
def analizar_texto(texto):
    """Analiza un texto y retorna sus estadísticas."""
    num_chars   = ___________
    palabras    = texto.split()
    num_palabras= ___________
    vocales     = 'aeiouáéíóuAEIOUÁÉÍÓÚ'
    num_vocales = ___________
    en_mayusc   = ___________
    primera     = palabras[0]
    ultima      = palabras[-1]
    return num_chars, num_palabras, num_vocales, en_mayusc, primera, ultima

oracion = "Python es el lenguaje del futuro"
chars, palabras, vocales, mayusc, primera, ultima = analizar_texto(oracion)

print(f"Texto:          {oracion}")
print(f"Caracteres:     {chars}")
print(f"Palabras:       {palabras}")
print(f"Vocales:        {vocales}")
print(f"Mayúsculas:     {mayusc}")
print(f"Primera/última: {primera} / {ultima}")
```
## Ejercicio 5.9 — Funciones con valores por defecto — Menú de restaurante

- Crea una función calcular_cuenta con los siguientes parámetros y defaults:
  -   → precio_plato (obligatorio), bebida=15.0, postre=0, propina_pct=10, iva=0.13.
- La función debe calcular y retornar el total final.
- Llama a la función de 4 maneras diferentes cambiando los defaults.
- Muestra cómo los argumentos por nombre permiten saltar parámetros.
```python
def calcular_cuenta(precio_plato, bebida=15.0, postre=0, propina_pct=10, iva=0.13):
    """Calcula la cuenta total de un restaurante."""
    subtotal = precio_plato + bebida + postre
    propina  = subtotal * (propina_pct / 100)
    base     = subtotal + propina
    monto_iva= ___________
    total    = ___________
    return total

# Llama de 4 formas diferentes:
# 1. Solo el plato (usa todos los defaults)
t1 = calcular_cuenta(85)

# 2. Plato + postre, sin bebida estándar
t2 = calcular_cuenta(85, postre=25)

# 3. Propina del 15%
t3 = calcular_cuenta(85, propina_pct=15)

# 4. Sin propina
t4 = calcular_cuenta(85, bebida=20, postre=18, propina_pct=0)

print(f"Solo plato:        Bs. {t1:.2f}")
print(f"Plato + postre:    Bs. {t2:.2f}")
print(f"Propina 15%:       Bs. {t3:.2f}")
print(f"Sin propina:       Bs. {t4:.2f}")
```

## Ejercicio 5.10 — Desafío: Librería de conversión de unidades

- Crea una librería completa de funciones de conversión con docstrings.
- Temperatura: celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin.
- Distancia: km_a_millas, millas_a_km, metros_a_pies.
- Peso: kg_a_libras, libras_a_kg.
- Crea una función convertir(valor, tipo_origen, tipo_destino) que use las anteriores según el tipo.
- Maneja conversiones no soportadas retornando None e imprimiendo un mensaje.

```python
# ═══ LIBRERÍA DE CONVERSIÓN ═══

# --- Temperatura ---
def celsius_a_fahrenheit(c):
    """Convierte °C a °F. Fórmula: F = C*9/5 + 32"""
    return ___________

def fahrenheit_a_celsius(f):
    return ___________

def celsius_a_kelvin(c):
    return ___________

# --- Distancia ---
def km_a_millas(km):   return km * 0.621371
def millas_a_km(mi):   return mi * 1.60934
def metros_a_pies(m):  return m  * 3.28084

# --- Peso ---
def kg_a_libras(kg):   return kg * 2.20462
def libras_a_kg(lb):   return lb * 0.453592

# --- Función principal ---
def convertir(valor, tipo_origen, tipo_destino):
    """Convierte un valor entre unidades soportadas."""
    conversiones = {
        ("celsius",    "fahrenheit"): celsius_a_fahrenheit,
        ("fahrenheit", "celsius"):    fahrenheit_a_celsius,
        ("celsius",    "kelvin"):     celsius_a_kelvin,
        ("km",         "millas"):     km_a_millas,
        ("millas",     "km"):         millas_a_km,
        ("metros",     "pies"):       metros_a_pies,
        ("kg",         "libras"):     kg_a_libras,
        ("libras",     "kg"):         libras_a_kg,
    }
    clave = (tipo_origen.lower(), tipo_destino.lower())
    if clave in conversiones:
        return conversiones[clave](valor)
    else:
        print(f"Conversión {tipo_origen}→{tipo_destino} no soportada.")
        return None

# Prueba la librería:
print(convertir(100,  "celsius",    "fahrenheit"))
print(convertir(5,    "km",         "millas"))
print(convertir(70,   "kg",         "libras"))
print(convertir(30,   "metros",     "km"))       # no soportada
```