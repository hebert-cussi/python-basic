# MÓDULO 6 — EJERCICIOS

## Ejercicio 6.1 — Mi primera lista — Gestión de compras

- Crea una lista vacía llamada carrito.
- Agrega 5 productos usando append().
- Muestra el primer y último producto usando índices positivos y negativos.
- Reemplaza el tercer producto por uno diferente.
- Elimina el segundo producto con remove().
- Muestra la lista final y su longitud.

```python
# Gestión de carrito de compras
carrito = []

# Agrega 5 productos:
carrito.append("___________")
carrito.append("___________")
carrito.append("___________")
carrito.append("___________")
carrito.append("___________")

# Muestra primero y último:
print(f"Primero: {carrito[___]}")
print(f"Último:  {carrito[___]}")

# Reemplaza el tercer producto:
carrito[___] = "Monitor"

# Elimina el segundo:
carrito.remove(___________)

print(f"Carrito final: {carrito}")
print(f"Total items:   {len(carrito)}")
```
## Ejercicio 6.2 — Slicing — Análisis de ventas semanales

- Dada la lista ventas = [1200, 850, 1500, 920, 1100, 780, 1350]  (L-D).
- Usando solo slicing (sin bucles), obtén y muestra:
  -   → Las ventas de lunes a miércoles (primeros 3 días).
  -   → Las ventas del fin de semana (últimos 2 días).
  -   → Las ventas de los días intermedios (martes a viernes).
  -   → La lista de ventas en orden inverso.
  -   → Ventas de días alternos (lunes, miércoles, viernes, domingo).

```python
ventas = [1200, 850, 1500, 920, 1100, 780, 1350]
#          Lun   Mar  Mié   Jue  Vie   Sáb  Dom

lun_mie     = ventas[___:___]
fin_semana  = ventas[___:]
intermedios = ventas[___:___]
invertida   = ventas[___]
alternos    = ventas[___:___:___]

print(f"Lun–Mié:      {lun_mie}")
print(f"Fin de semana:{fin_semana}")
print(f"Intermedios:  {intermedios}")
print(f"Invertida:    {invertida}")
print(f"Alternos:     {alternos}")
print(f"Total semana: Bs. {sum(ventas):,.0f}")
```

## Ejercicio 6.3 — Métodos de lista — Sistema de ranking

- Crea una lista de notas: [72, 88, 65, 95, 81, 59, 77, 90].
- Usa métodos para:
  -   → Ordenar de mayor a menor (sin modificar la original — usa sorted()).
  -   → Encontrar la posición de la nota 81 con index().
  -   → Agregar la nota 84 y luego insertar 91 en la posición 2.
  -   → Contar cuántas veces aparece el número 88 con count().
  -   → Eliminar la nota más baja con pop() tras encontrar su índice.
- Muestra el ranking final numerado con enumerate().

```python
notas = [72, 88, 65, 95, 81, 59, 77, 90]

ranking     = sorted(notas, reverse=___________)
pos_81      = notas.index(___________)

notas.___________(84)          # agregar al final
notas.___________(2, 91)       # insertar en posición 2
veces_88    = notas.count(___________)

# Eliminar la nota más baja
pos_min     = notas.index(min(notas))
eliminada   = notas.pop(___________)

print(f"Nota 81 en posición: {pos_81}")
print(f"Veces 88: {veces_88}")
print(f"Eliminada: {eliminada}")
print("\nRanking final:")
for pos, nota in enumerate(sorted(notas, reverse=True), start=1):
    print(f"  {pos}. {nota}")
```

## Ejercicio 6.4 — Desafío: Gestión de inventario con listas

- Crea dos listas paralelas: productos y precios (al menos 6 ítems).
- Implementa las siguientes operaciones usando métodos de lista:
  -   → Mostrar el inventario completo con enumerate() (número, producto, precio).
  -   → Buscar un producto por nombre e indicar su precio y posición.
  -   → Actualizar el precio de un producto por su nombre.
  -   → Eliminar un producto (y su precio correspondiente) por nombre.
  -   → Mostrar el producto más caro y el más barato.
  -   → Calcular el valor total del inventario.

```python
# Inventario con listas paralelas
productos = ["Laptop","Mouse","Teclado","Monitor","Audífonos","Webcam"]
precios   = [3500.0, 85.0, 220.0, 1200.0, 350.0, 280.0]

# 1. Mostrar inventario
print("=== INVENTARIO ===")
for i, (prod, precio) in enumerate(zip(productos, precios), 1):
    print(f"{i:>2}. {prod:<12} Bs. {precio:>8,.2f}")

# 2. Buscar producto
buscar = input("\nBuscar producto: ")
if buscar in productos:
    idx = productos.index(___________)
    print(f"Encontrado en posición {idx} — Bs. {precios[idx]:.2f}")
else:
    print("No encontrado")

# 3. Actualizar precio
actualizar = input("Producto a actualizar: ")
if actualizar in productos:
    idx = productos.index(actualizar)
    nuevo = float(input("Nuevo precio: "))
    precios[___________] = nuevo

# 4. Eliminar producto
eliminar = input("Producto a eliminar: ")
if eliminar in productos:
    idx = productos.index(eliminar)
    productos.pop(___________)
    precios.pop(___________)

# 5. Estadísticas
idx_max = precios.index(max(precios))
idx_min = precios.index(min(precios))
print(f"Más caro:  {productos[idx_max]} — Bs. {max(precios):.2f}")
print(f"Más barato:{productos[idx_min]} — Bs. {min(precios):.2f}")
print(f"Total inventario: Bs. {sum(precios):,.2f}")
```

## Ejercicio 6.5 — Recorrido con enumerate() y acumuladores

- Dada la lista de temperaturas diarias de La Paz (en °C):
- temps = [12, 15, 8, 18, 22, 11, 9, 16, 20, 14, 7, 13]
- Usando un bucle for con enumerate(), calcula y muestra:
  -   → Temperatura promedio del mes.
  -   → El día más caluroso y el más frío (con su número de día).
  -   → Cuántos días superaron los 15°C.
  -   → Lista de temperaturas por encima del promedio.

```python
temps = [12, 15, 8, 18, 22, 11, 9, 16, 20, 14, 7, 13]

total      = 0
dia_max    = (0, temps[0])   # (número de día, temperatura)
dia_min    = (0, temps[0])
dias_calur = 0
sobre_prom = []

promedio = sum(temps) / len(temps)

for dia, temp in enumerate(temps, start=1):
    total += temp

    if temp > dia_max[1]:
        dia_max = (dia, ___________)
    if temp < dia_min[1]:
        dia_min = (dia, ___________)
    if temp > 15:
        dias_calur += ___________
    if temp > promedio:
        sobre_prom.___________(temp)

print(f"Promedio:       {promedio:.1f}°C")
print(f"Día más calur.: Día {dia_max[0]} — {dia_max[1]}°C")
print(f"Día más frío:   Día {dia_min[0]} — {dia_min[1]}°C")
print(f"Días > 15°C:    {dias_calur}")
print(f"Sobre promedio: {sobre_prom}")
```

## Ejercicio 6.6 — Matrices con listas anidadas

- Crea una matriz 4×4 de números del 1 al 16.
- Usando bucles anidados muestra la matriz formateada.
- Calcula la suma de cada fila y de cada columna.
- Calcula la diagonal principal (elementos donde fila == columna).
- Encuentra el elemento mayor de toda la matriz.

```python
# Crear la matriz 4x4
matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

# Mostrar la matriz
print("Matriz 4x4:")
for fila in matriz:
    for elem in fila:
        print(f"{elem:>4}", end="")
    print()

# Suma de filas
print("\nSuma por fila:")
for i, fila in enumerate(matriz):
    print(f"  Fila {i}: {sum(fila)}")

# Suma de columnas
print("Suma por columna:")
for col in range(4):
    suma_col = sum(matriz[fila][col] for fila in range(4))
    print(f"  Col {col}: {suma_col}")

# Diagonal principal
diagonal = [matriz[i][i] for i in range(4)]
print(f"Diagonal: {diagonal}  Suma: {sum(diagonal)}")

# Elemento mayor
mayor = max(max(fila) for fila in matriz)
print(f"Mayor elemento: {mayor}")
```

## Ejercicio 6.7 — Tuplas — Datos de ciudades bolivianas

- Crea una lista de tuplas donde cada tupla represente una ciudad boliviana:
  -   → (nombre, departamento, altitud_msnm, poblacion)
- Incluye al menos 5 ciudades.
- Recorre la lista e imprime la información de cada ciudad con formato.
- Encuentra la ciudad más alta y la más poblada.
- Usa desempaquetado de tuplas en el bucle for.

```python
# Lista de tuplas: (ciudad, depto, altitud, poblacion)
ciudades = [
    ("La Paz",       "La Paz",       3625, 835361),
    ("Cochabamba",   "Cochabamba",   2558, 630587),
    ("Santa Cruz",   "Santa Cruz",    416, 1453549),
    ("Oruro",        "Oruro",         3706, 264683),
    ("Potosí",       "Potosí",        3967, 189652),
]

# Mostrar todas las ciudades
print('Ciudad         Depto        Altitud    Población')
print("-" * 50)
for ciudad, depto, alt, pob in ciudades:
    print(f"{ciudad:<15} {depto:<12} {alt:>7}m {pob:>10,}")

# Ciudad más alta
mas_alta = max(ciudades, key=lambda c: c[___])
print(f"\nMás alta: {mas_alta[0]} a {mas_alta[2]} msnm")

# Ciudad más poblada
mas_pob  = max(ciudades, key=lambda c: c[___])
print(f"Más poblada: {mas_pob[0]} con {mas_pob[3]:,} hab.")
```

## Ejercicio 6.8 — Estadísticas de lista sin funciones incorporadas	Medio

- Crea una función estadisticas_manual(numeros) que calcule:
  -   → Suma total (usando for, sin sum()).
  -   → Promedio (suma / cantidad).
  -   → Máximo y mínimo (sin max() ni min()).
  -   → Rango (máximo - mínimo).
  -   → Mediana (ordenar la lista y tomar el valor del centro).
- Prueba la función con la lista: [34, 67, 12, 89, 45, 23, 78, 56].

```python
def estadisticas_manual(numeros):
    """Calcula estadísticas sin usar funciones incorporadas."""
    # Suma
    total = 0
    for n in numeros:
        total += ___________

    cantidad = len(numeros)
    promedio = ___________

    # Máximo y mínimo
    maximo = numeros[0]
    minimo = numeros[0]
    for n in numeros:
        if n > maximo: maximo = n
        if n < minimo: minimo = ___________

    rango = ___________

    # Mediana
    ordenada = sorted(numeros)
    mid = len(ordenada) // 2
    if len(ordenada) % 2 == 0:
        mediana = (ordenada[mid-1] + ordenada[mid]) / 2
    else:
        mediana = ___________

    return total, promedio, maximo, minimo, rango, mediana

datos = [34, 67, 12, 89, 45, 23, 78, 56]
t,p,mx,mn,r,med = estadisticas_manual(datos)
print(f"Total:    {t}")
print(f"Promedio: {p:.2f}")
print(f"Máximo:   {mx}  Mínimo: {mn}")
print(f"Rango:    {r}")
print(f"Mediana:  {med}")
```
## Ejercicio 6.9 — Desafío: Filtros y transformaciones de listas

- Dada la lista de ventas diarias del mes (30 valores entre 500 y 3000):
- ventas = [1200,850,1500,920,1100,780,1350,2100,650,1800,990,1450,2200,750,1650,880,1950,1100,2350,700,1400,830,1750,1250,960,2050,1600,890,1300,1700]
- Sin usar list comprehensions, crea funciones para obtener:
  - → filtrar_mayores(ventas, umbral): lista de ventas > umbral.
  - → aplicar_descuento(ventas, pct): lista con cada venta reducida en pct%.
  - → semanas(ventas): lista de 4 sublistas de 7 elementos (semanas del mes).
  - → top_n(ventas, n): los n valores más altos ordenados.

ventas = [1200,850,1500,920,1100,780,1350,2100,650,1800,
          990,1450,2200,750,1650,880,1950,1100,2350,700,
          1400,830,1750,1250,960,2050,1600,890,1300,1700]
```python
def filtrar_mayores(ventas, umbral):
    resultado = []
    for v in ventas:
        if v > umbral:
            resultado.___________(v)
    return resultado

def aplicar_descuento(ventas, pct):
    resultado = []
    for v in ventas:
        resultado.append(v * (1 - pct/100))
    return resultado

def semanas(ventas):
    return [ventas[i*7:(i+1)*7] for i in range(4)]

def top_n(ventas, n):
    return sorted(ventas, reverse=True)[:n]

# Prueba todas las funciones:
altas    = filtrar_mayores(ventas, 1500)
desc_10  = aplicar_descuento(ventas, 10)
por_sem  = semanas(ventas)
top5     = top_n(ventas, 5)

print(f"Ventas > 1500: {len(altas)} días")
print(f"Con desc 10%: Bs. {sum(desc_10):,.0f} total")
for i, sem in enumerate(por_sem, 1):
    print(f"  Semana {i}: Bs. {sum(sem):,.0f}")
print(f"Top 5: {top5}")
```
## Ejercicio 6.10 — Desafío: Sistema de notas con listas y tuplas

- Combina todo el módulo en un sistema de notas estudiantiles.
- Almacena los estudiantes como tuplas: (nombre, matrícula).
- Almacena sus notas en una lista de listas (una sublista por estudiante, 4 notas).
- Implementa funciones para: calcular promedio de cada estudiante, generar ranking, mostrar estadísticas del grupo.
- Usa slicing para obtener los 3 mejores y los 3 peores estudiantes.
- Muestra todo en un reporte formateado.

```python
# Tuplas de estudiantes (inmutables)
estudiantes = [
    ("Ana López",    "2024-001"),
    ("Carlos Ramos", "2024-002"),
    ("María Quispe", "2024-003"),
    ("Luis Torrez",  "2024-004"),
    ("Sofia Vargas", "2024-005"),
]

# Notas como lista mutable (4 notas por estudiante)
notas = [
    [85, 92, 78, 88],
    [62, 55, 70, 58],
    [95, 88, 92, 97],
    [74, 81, 68, 77],
    [90, 85, 93, 87],
]

def calcular_promedio(notas_est):
    return sum(notas_est) / len(notas_est)

# Calcular promedios y crear ranking
promedios = [calcular_promedio(n) for n in notas]
ranking   = sorted(zip(promedios, estudiantes), reverse=True)

# Reporte
print("="*50)
print(f"  REPORTE FINAL — PYTHON BÁSICO")
print("-"*50)
for pos, (prom, (nombre, mat)) in enumerate(ranking, 1):
    est = 'Aprobado' if prom >= 51 else 'Reprobado'
    print(f"{pos}. {nombre:<15} {mat}  {prom:.1f}  {est}")

# Estadísticas con slicing
mejores = ranking[:3]
peores  = ranking[-3:]
print(f"\nTop 3:  {[e[1][0] for e in mejores]}")
print(f"Bottom 3: {[e[1][0] for e in peores]}")
print(f"Promedio grupal: {sum(promedios)/len(promedios):.1f}")
 ```