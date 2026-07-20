# MÓDULO 7 — EJERCICIOS
## Ejercicio 7.1 — Mi primer diccionario — Ficha de contacto

- Crea un diccionario llamado contacto con al menos 6 claves: nombre, apellido, telefono, email, ciudad, activo.
- Accede e imprime cada valor usando corchetes y usando get().
- Agrega dos nuevos pares clave-valor: fecha_nacimiento y profesion.
- Modifica la ciudad y el teléfono.
- Elimina el campo activo con pop() e imprime el valor que retorna.
- Muestra el diccionario final y verifica si 'email' existe con el operador in.

```python
# Ficha de contacto
contacto = {
    "nombre":   "___________",
    "apellido": "___________",
    "telefono": "___________",
    "email":    "___________",
    "ciudad":   "___________",
    "activo":   True
}

# Acceder con corchetes y get()
print(contacto["nombre"])
print(contacto.get("email", "Sin email"))

# Agregar nuevos campos
contacto["fecha_nacimiento"] = "___________"
contacto["profesion"]        = "___________"

# Modificar
contacto["ciudad"]   = "___________"
contacto["telefono"] = "___________"

# Eliminar con pop()
eliminado = contacto.pop("activo")
print(f"Valor eliminado: {eliminado}")

print(f"\nContacto final: {contacto}")
print(f"¿Tiene email? {'email' in contacto}")
```

## Ejercicio 7.2 — Recorrer diccionarios con keys, values e items

- Dado el diccionario de precios de productos, recórrelo de 3 maneras diferentes:
 - → Con .keys(): imprime solo los nombres de los productos.
 - → Con .values(): imprime solo los precios formateados con 2 decimales.
 - → Con .items(): imprime cada producto con su precio en formato de factura.
- Calcula el total, el precio promedio, el producto más caro y el más barato.

```python
precios = {
    "Laptop HP":   3500.0,
    "Mouse USB":     85.0,
    "Teclado":      220.0,
    "Monitor 24":  1200.0,
    "Audífonos":    350.0,
    "Webcam":       280.0,
}

# 1. Solo claves
print("Productos disponibles:")
for producto in precios.___________():
    print(f"  - {producto}")

# 2. Solo valores
print("\nLista de precios:")
for precio in precios.___________():
    print(f"  Bs. {precio:,.2f}")

# 3. Pares clave-valor
print("\nCatálogo completo:")
for producto, precio in precios.___________():
    print(f"  {producto:<15} Bs. {precio:>8,.2f}")

# Estadísticas
total   = sum(precios.values())
prom    = total / len(precios)
mas_car = max(precios, key=precios.get)
mas_bar = min(precios, key=precios.get)
print(f"\nTotal: Bs. {total:,.2f}  Prom: Bs. {prom:,.2f}")
print(f"Más caro:   {mas_car} — Bs. {precios[mas_car]:,.2f}")
print(f"Más barato: {mas_bar} — Bs. {precios[mas_bar]:,.2f}")
```

## Ejercicio 7.3 — Contador de palabras con diccionario

- Dado un texto, cuenta cuántas veces aparece cada palabra.
- Normaliza el texto a minúsculas y elimina signos de puntuación antes de contar.
- Usa un diccionario donde la clave es la palabra y el valor es el conteo.
- Muestra las 5 palabras más frecuentes ordenadas de mayor a menor.
- Muestra cuántas palabras únicas tiene el texto.

```python
texto = "Python es un lenguaje de programacion Python es popular la programacion con Python es divertida Python tiene muchas librerias"

# Normalizar y dividir
palabras = texto.lower().split()

# Contar con diccionario
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += ___________
    else:
        conteo[palabra]  = ___________

# Alternativa con get():
# conteo[palabra] = conteo.get(palabra, 0) + 1

# Ordenar por frecuencia descendente
ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

print(f"Palabras únicas: {len(conteo)}")
print("\nTop 5 más frecuentes:")
for palabra, veces in ordenado[:5]:
    print(f"  {palabra:<15} {veces} vez/veces")
```

## Ejercicio 7.4 — Desafío: Sistema de notas con diccionario anidado

- Crea un diccionario de estudiantes donde cada clave es el número de matrícula.
- Cada valor es un diccionario con: nombre, notas (lista), promedio calculado.
- Implementa funciones para: agregar estudiante, agregar nota, calcular promedio automático.
- Muestra el ranking ordenado por promedio descendente.
- Usa update() para modificar datos de un estudiante existente.

```python
def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

def agregar_estudiante(registro, matricula, nombre):
    registro[matricula] = {"nombre": nombre, "notas": [], "promedio": 0}

def agregar_nota(registro, matricula, nota):
    if matricula in registro:
        registro[matricula][___________].append(nota)
        registro[matricula][___________] = calcular_promedio(
            registro[matricula]['notas']
        )
    else:
        print(f"Matrícula {matricula} no encontrada")

# Crear registro y agregar datos
registro = {}
agregar_estudiante(registro, "2024-001", "Ana López")
agregar_estudiante(registro, "2024-002", "Carlos Ramos")
agregar_estudiante(registro, "2024-003", "María Quispe")

for nota in [85, 92, 78, 88]: agregar_nota(registro, "2024-001", nota)
for nota in [62, 70, 55, 68]: agregar_nota(registro, "2024-002", nota)
for nota in [95, 88, 92, 97]: agregar_nota(registro, "2024-003", nota)

# Ranking
ranking = sorted(registro.items(), key=lambda x: x[1]['promedio'], reverse=True)
print("=== RANKING ===")
for pos, (mat, datos) in enumerate(ranking, 1):
    print(f"{pos}. {datos['nombre']:<15} {datos['promedio']:.1f}")

```

## Ejercicio 7.5 — Eliminar duplicados y pertenencia

- Dada la lista de compras con artículos repetidos, usa un set para eliminar duplicados.
- Compara la longitud de la lista original vs el conjunto resultante.
- Verifica si ciertos artículos están en la lista usando 'in' (compara velocidad).
- Convierte el conjunto de vuelta a lista ordenada.

```python
compras = ['leche','pan','huevos','leche','arroz','pan',
           'azúcar','aceite','leche','huevos','sal','pan']

print(f"Lista original: {len(compras)} items")

# Eliminar duplicados con set
unicos = ___________
print(f"Sin duplicados: {len(unicos)} items")
print(f"Duplicados eliminados: {len(compras) - len(unicos)}")

# Verificar pertenencia
buscar = ['leche', 'mantequilla', 'arroz', 'yogur']
for item in buscar:
    presente = item in unicos
    print(f"  {item:<15} → {'✅ En lista' if presente else '❌ No está'}")

# Convertir a lista ordenada
lista_ordenada = sorted(___________)
print(f"\nLista de compras ordenada: {lista_ordenada}")
```

## Ejercicio 7.6 — Operaciones de conjuntos — Análisis de audiencia

- Una empresa tiene 3 grupos de clientes según sus suscripciones:
  -   → clientes_email: clientes con suscripción a email marketing.
  -   → clientes_sms: clientes con suscripción a SMS.
  -   → clientes_app: clientes con la app instalada.
- Usando operaciones de conjuntos, determina:
  -   → Clientes con TODAS las suscripciones (intersección triple).
  -   → Clientes con AL MENOS UNA suscripción (unión).
  -   → Clientes SOLO con email (no en sms ni app).
  -   → Clientes sin ninguna suscripción (dado un conjunto total de 'todos_clientes').

```python
clientes_email = {'Ana','Carlos','María','Luis','Pedro','Sofía'}
clientes_sms   = {'Carlos','María','Pedro','Jorge','Laura'}
clientes_app   = {'Ana','María','Luis','Laura','Carmen','Diego'}
todos_clientes = {'Ana','Carlos','María','Luis','Pedro','Sofía',
                  'Jorge','Laura','Carmen','Diego','Pablo','Rosa'}

# Operaciones
todas_subs    = clientes_email ___ clientes_sms ___ clientes_app
alguna_sub    = clientes_email ___ clientes_sms ___ clientes_app
solo_email    = clientes_email ___ clientes_sms ___ clientes_app
sin_sub       = todos_clientes ___ alguna_sub

print(f"Con todas las suscripciones ({len(todas_subs)}): {todas_subs}")
print(f"Con alguna suscripción ({len(alguna_sub)}): {alguna_sub}")
print(f"Solo email ({len(solo_email)}): {solo_email}")
print(f"Sin suscripción ({len(sin_sub)}): {sin_sub}")
```

## Ejercicio 7.7 — Comparar colecciones con conjuntos

- Tienes las listas de asistencia de dos días de clase.
- Usando conjuntos, determina: quién asistió ambos días, quién solo fue un día, quién faltó ambos días.
- Calcula el porcentaje de asistencia para cada estudiante.
- Usa issubset() para verificar si el grupo completo asistió al menos un día.

```python
grupo_total = {'Ana','Carlos','María','Luis','Pedro','Sofía','Jorge','Laura'}
asistencia_lunes  = {'Ana','Carlos','María','Pedro','Sofía','Jorge'}
asistencia_martes = {'Ana','María','Luis','Pedro','Laura','Jorge'}

# Calcula con operaciones de sets
asistio_ambos   = asistencia_lunes ___ asistencia_martes
solo_lunes      = asistencia_lunes ___ asistencia_martes
solo_martes     = asistencia_martes ___ asistencia_lunes
falto_ambos     = grupo_total ___ (asistencia_lunes ___ asistencia_martes)

print(f"Asistió ambos días ({len(asistio_ambos)}):    {asistio_ambos}")
print(f"Solo lunes ({len(solo_lunes)}):         {solo_lunes}")
print(f"Solo martes ({len(solo_martes)}):        {solo_martes}")
print(f"Faltó ambos días ({len(falto_ambos)}):   {falto_ambos}")

# Verificar asistencia mínima
alguna_vez = asistencia_lunes | asistencia_martes
todos_asistieron = grupo_total.issubset(___________)
print(f"¿Todos asistieron al menos un día? {todos_asistieron}")
```

## Ejercicio 7.8 — Agenda de contactos con diccionario

- Crea una agenda de contactos interactiva con las siguientes operaciones:
  -  → Agregar contacto (nombre, teléfono, email, grupo).
  -  → Buscar contacto por nombre (parcial o completo).
  -  → Listar contactos por grupo usando un diccionario auxiliar.
  -  → Mostrar todos los grupos únicos disponibles (usando set).
  -  → Exportar resumen: total de contactos y contactos por grupo.
```python
agenda = {}

def agregar_contacto(agenda, nombre, telefono, email, grupo):
    agenda[nombre] = {"telefono":telefono,"email":email,"grupo":grupo}

def buscar_contacto(agenda, termino):
    resultados = {}
    for nombre, datos in agenda.items():
        if termino.lower() in nombre.lower():
            resultados[nombre] = datos
    return resultados

def listar_por_grupo(agenda):
    grupos = {}
    for nombre, datos in agenda.items():
        g = datos['grupo']
        if g not in grupos:
            grupos[g] = []
        grupos[g].___________(nombre)
    return grupos

# Agregar contactos de prueba
agregar_contacto(agenda,"Ana López","70012345","ana@mail.com","Trabajo")
agregar_contacto(agenda,"Carlos Ramos","71023456","carlos@mail.com","Familia")
agregar_contacto(agenda,"María Quispe","72034567","maria@mail.com","Trabajo")
agregar_contacto(agenda,"Luis Torrez","73045678","luis@mail.com","Amigos")

# Usar las funciones
encontrados = buscar_contacto(agenda, "a")
print(f"Contactos con 'a': {list(encontrados.keys())}")

grupos = listar_por_grupo(agenda)
for grupo, contactos in grupos.items():
    print(f"{grupo}: {contactos}")

grupos_unicos = {d['grupo'] for d in agenda.values()}
print(f"Grupos disponibles: {grupos_unicos}")
```

## Ejercicio 7.9 — Desafío: Análisis de ventas con diccionarios

- Dado un registro de ventas diarias (lista de diccionarios), realiza un análisis completo:
  -  → Agrupar ventas por vendedor y calcular total por vendedor.
  -  → Agrupar ventas por categoría y calcular total por categoría.
  -  → Encontrar el vendedor estrella (mayor total).
  -  → Encontrar la categoría más rentable.
  -  → Calcular el ticket promedio (monto promedio por venta).

```python
ventas = [
    {"vendedor":"Ana",    "categoria":"Electrónica","monto":3500},
    {"vendedor":"Carlos", "categoria":"Ropa",       "monto":450},
    {"vendedor":"Ana",    "categoria":"Ropa",       "monto":280},
    {"vendedor":"María",  "categoria":"Electrónica","monto":1200},
    {"vendedor":"Carlos", "categoria":"Electrónica","monto":850},
    {"vendedor":"María",  "categoria":"Hogar",      "monto":320},
    {"vendedor":"Ana",    "categoria":"Hogar",      "monto":650},
    {"vendedor":"Carlos", "categoria":"Ropa",       "monto":190},
]

# Por vendedor
por_vendedor = {}
for venta in ventas:
    v = venta['vendedor']
    por_vendedor[v] = por_vendedor.get(v, 0) + venta[___________]

# Por categoría
por_cat = {}
for venta in ventas:
    c = venta['categoria']
    por_cat[c] = por_cat.get(c, 0) + venta['monto']

# Estadísticas
estrella   = max(por_vendedor, key=por_vendedor.get)
cat_top    = max(por_cat,      key=por_cat.get)
ticket_prom= sum(v['monto'] for v in ventas) / len(ventas)

print("Ventas por vendedor:")
for v, total in sorted(por_vendedor.items(), key=lambda x: x[1], reverse=True):
    print(f"  {v:<10} Bs. {total:,.0f}")
print(f"\nVendedor estrella: {estrella}")
print(f"Categoría top:     {cat_top}")
print(f"Ticket promedio:   Bs. {ticket_prom:,.0f}")
```
## Ejercicio 7.10 — Desafío: Inventario inteligente con dict y sets

- Combina diccionarios, conjuntos y listas para gestionar el inventario de una tienda.
- El inventario es un dict anidado con código, nombre, precio, stock y categoría.
- Usa sets para: obtener categorías únicas, encontrar productos sin stock, comparar con proveedor.
- Implementa funciones para: buscar por categoría, aplicar descuento por categoría, reabastecer stock.
- Genera un reporte completo del estado del inventario.

```python
inventario = {
    "P001":{"nombre":"Laptop","precio":3500,"stock":5,"categoria":"comp"},
    "P002":{"nombre":"Mouse", "precio":85,  "stock":0,"categoria":"perf"},
    "P003":{"nombre":"Teclado","precio":220,"stock":12,"categoria":"perf"},
    "P004":{"nombre":"Monitor","precio":1200,"stock":3,"categoria":"comp"},
    "P005":{"nombre":"Audífonos","precio":350,"stock":0,"categoria":"audio"},
}

def categorias_disponibles(inv):
    return {p['categoria'] for p in inv.values()}

def productos_sin_stock(inv):
    return {k for k,v in inv.items() if v['stock'] == ___________}

def buscar_por_categoria(inv, cat):
    return {k:v for k,v in inv.items() if v['categoria'] == cat}

def aplicar_descuento(inv, categoria, pct):
    for datos in inv.values():
        if datos['categoria'] == categoria:
            datos['precio'] *= (1 - pct/100)

# Usar las funciones
cats  = categorias_disponibles(inventario)
s_stk = productos_sin_stock(inventario)
comps = buscar_por_categoria(inventario, 'comp')

print(f"Categorías: {cats}")
print(f"Sin stock: {s_stk}")
print(f"Computación: {[v['nombre'] for v in comps.values()]}")

aplicar_descuento(inventario, 'perf', 10)

print("\n=== REPORTE FINAL ===")
for cod, datos in inventario.items():
    estado = 'OK' if datos['stock'] > 0 else 'SIN STOCK'
    print(f"{cod} {datos['nombre']:<12} Bs.{datos['precio']:>8,.0f} [{estado}]")
```