# MÓDULO 8 — EJERCICIOS

## Ejercicio 8.1 — Calculadora segura con manejo de errores	

- Crea una función calculadora(a, b, operacion) que acepte: '+', '-', '*', '/'.
- Maneja con try/except los siguientes errores: ZeroDivisionError, TypeError, ValueError.
- Usa else para mostrar el resultado solo si no hubo error.
- Usa finally para siempre mostrar el mensaje 'Operación procesada.'.
- Prueba la función con al menos 5 llamadas incluyendo casos de error.

```python
def calculadora(a, b, operacion):
    """Calculadora segura con manejo de errores."""
    try:
        if operacion == "+":  resultado = a + b
        elif operacion == "-": resultado = a - b
        elif operacion == "*": resultado = a * b
        elif operacion == "/": resultado = a / b
        else:
            raise ValueError(f"Operación '{operacion}' no válida")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
        return None
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return None
    except ValueError as e:
        print(f"Error de valor: {e}")
        return None
    else:
        print(f"Resultado: {a} {operacion} {b} = {resultado}")
        return resultado
    finally:
        print("Operación procesada.")

# Prueba con 5 casos:
calculadora(10, 3, "+")    # ✅ normal
calculadora(10, 0, "/")    # ❌ ZeroDivisionError
calculadora("5", 2, "*")   # ❌ TypeError
calculadora(10, 3, "%")    # ❌ ValueError
calculadora(15, 4, "/")    # ✅ 3.75
```
## Ejercicio 8.2 — Validador de entrada de usuario

- Crea una función pedir_entero(mensaje, minimo, maximo) que:
  - → Solicite un número entero al usuario con input().
  - → Use try/except para capturar ValueError si no ingresa un número.
  - → Valide que esté dentro del rango [minimo, maximo], lanzando ValueError si no.
  - → Repita hasta obtener un valor válido (bucle while).
- Crea también pedir_float(mensaje) y pedir_opcion(mensaje, opciones_validas).
```python
def pedir_entero(mensaje, minimo=None, maximo=None):
    """Solicita un entero válido dentro de un rango opcional."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                raise ValueError(f"Mínimo permitido: {minimo}")
            if maximo is not None and valor > maximo:
                raise ValueError(f"Máximo permitido: {maximo}")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intenta de nuevo.")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un número decimal. Intenta de nuevo.")

def pedir_opcion(mensaje, opciones):
    while True:
        resp = input(mensaje).strip().lower()
        if resp in opciones:
            return resp
        print(f"Opción inválida. Opciones válidas: {opciones}")

# Prueba:
edad  = pedir_entero("Edad (1-120): ", 1, 120)
nota  = pedir_float("Nota (0.0-100.0): ")
resp  = pedir_opcion("¿Continuar? (s/n): ", ["s","n"])
print(f"Edad: {edad}, Nota: {nota}, Resp: {resp}")
```

## Ejercicio 8.3 — Manejo de errores personalizado con raise

- Crea excepciones personalizadas para un sistema de banco:
  -   → SaldoInsuficienteError: cuando el retiro supera el saldo.
  -   → MontoInvalidoError: cuando el monto es negativo o cero.
  -   → CuentaBloqueadaError: cuando la cuenta está bloqueada.
- Implementa las funciones depositar, retirar y verificar_estado usando raise y try/except.

```python
# Excepciones personalizadas
class SaldoInsuficienteError(Exception):
    pass

class MontoInvalidoError(Exception):
    pass

class CuentaBloqueadaError(Exception):
    pass

# Cuenta bancaria
cuenta = {'saldo': 1000.0, 'bloqueada': False}

def depositar(monto):
    if monto <= 0:
        raise MontoInvalidoError(f"Monto inválido: {monto}")
    cuenta['saldo'] += monto
    print(f"Depósito de Bs. {monto:.2f}. Saldo: Bs. {cuenta['saldo']:.2f}")

def retirar(monto):
    if cuenta['bloqueada']:
        raise CuentaBloqueadaError("La cuenta está bloqueada")
    if monto <= 0:
        raise MontoInvalidoError("El monto debe ser positivo")
    if monto > cuenta['saldo']:
        raise SaldoInsuficienteError(
            f"Saldo insuficiente. Disponible: Bs. {cuenta['saldo']:.2f}")
    cuenta['saldo'] -= monto
    print(f"Retiro de Bs. {monto:.2f}. Saldo: Bs. {cuenta['saldo']:.2f}")

# Prueba con manejo de errores:
for operacion in [('depositar',500),('retirar',200),('retirar',2000),('retirar',-50)]:
    try:
        if operacion[0]=="depositar": depositar(operacion[1])
        else: retirar(operacion[1])
    except (SaldoInsuficienteError, MontoInvalidoError, CuentaBloqueadaError) as e:
        print(f"Error bancario: {e}")
```

## Ejercicio 8.4 — Desafío: Decorador de manejo de errores

- Crea un decorador llamado manejo_seguro que envuelva cualquier función en un try/except.
- El decorador debe: capturar cualquier excepción, registrar el error en un archivo 'errores.log' con fecha/hora, y retornar None si hay error.
- Aplica el decorador a 3 funciones diferentes que puedan fallar.
- El log debe incluir: fecha, nombre de la función, tipo de error y mensaje.

```python
import functools
from datetime import datetime

def manejo_seguro(func):
    """Decorador que captura errores y los registra en un log."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            mensaje_error = (
                f"[{timestamp}] {func.__name__}: "
                f"{type(e).__name__}: {e}\n"
            )
            # Registrar en archivo de log
            with open('errores.log', 'a', encoding='utf-8') as log:
                log.write(mensaje_error)
            print(f"Error registrado en errores.log: {e}")
            return None
    return wrapper

@manejo_seguro
def dividir(a, b):
    return a / b

@manejo_seguro
def convertir_entero(texto):
    return int(texto)

@manejo_seguro
def acceder_lista(lista, indice):
    return lista[indice]

# Prueba:
print(dividir(10, 2))         # 5.0
print(dividir(10, 0))         # Error → None
print(convertir_entero("abc"))# Error → None
print(acceder_lista([1,2],10))# Error → None
```

## Ejercicio 8.5 — Agenda personal en archivo de texto

- Crea un sistema de agenda que guarde contactos en un archivo 'agenda.txt'.
- Implementa las funciones: agregar_contacto, leer_contactos, buscar_contacto.
- Cada línea del archivo tendrá el formato: nombre|telefono|email.
- Al leer, convierte cada línea en un diccionario.
- Maneja FileNotFoundError si el archivo no existe al leer.
```python
ARCHIVO_AGENDA = 'agenda.txt'

def agregar_contacto(nombre, telefono, email):
    try:
        with open(ARCHIVO_AGENDA, 'a', encoding='utf-8') as f:
            f.write(f"{nombre}|{telefono}|{email}\n")
        print(f"Contacto {nombre} agregado.")
    except IOError as e:
        print(f"Error al escribir: {e}")

def leer_contactos():
    contactos = []
    try:
        with open(ARCHIVO_AGENDA, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split('|')
                    if len(partes) == 3:
                        contactos.append({
                            "nombre":   partes[0],
                            "telefono": partes[1],
                            "email":    partes[2]
                        })
    except FileNotFoundError:
        print("La agenda está vacía o no existe.")
    return contactos

def buscar_contacto(termino):
    contactos = leer_contactos()
    return [c for c in contactos if termino.lower() in c['nombre'].lower()]

# Prueba:
agregar_contacto("Ana López",    "70012345", "ana@mail.com")
agregar_contacto("Carlos Ramos", "71023456", "carlos@mail.com")
agregar_contacto("María Quispe", "72034567", "maria@mail.com")

todos = leer_contactos()
for c in todos:
    print(f"  {c['nombre']} — {c['telefono']}")

encontrados = buscar_contacto("ana")
print(f"Buscando 'ana': {[c['nombre'] for c in encontrados]}")
```

## Ejercicio 8.6 — Diario personal con JSON y datetime

- Crea un diario personal que guarde entradas en un archivo 'diario.json'.
- Cada entrada tendrá: id (auto-incremental), fecha (datetime automática), titulo, contenido.
- Implementa: nueva_entrada, leer_entradas, buscar_por_fecha.
- Usa json.dump con indent=4 para formato legible.
- Muestra las entradas ordenadas por fecha de más reciente a más antigua.

```python
import json
import os
from datetime import datetime

ARCHIVO_DIARIO = 'diario.json'

def cargar_diario():
    if os.path.exists(ARCHIVO_DIARIO):
        with open(ARCHIVO_DIARIO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_diario(entradas):
    with open(ARCHIVO_DIARIO, 'w', encoding='utf-8') as f:
        json.dump(entradas, f, ensure_ascii=False, indent=4)

def nueva_entrada(titulo, contenido):
    entradas = cargar_diario()
    nueva = {
        'id':        len(entradas) + 1,
        "fecha":     datetime.now().strftime("%d/%m/%Y %H:%M"),
        "titulo":    titulo,
        "contenido": contenido
    }
    entradas.append(nueva)
    guardar_diario(entradas)
    print(f"Entrada #{nueva['id']} guardada.")

def leer_entradas():
    entradas = cargar_diario()
    print(f"\n=== MI DIARIO ({len(entradas)} entradas) ===")
    for e in reversed(entradas):   # más recientes primero
        print(f"\n[{e['fecha']}] #{e['id']} — {e['titulo']}")
        print(f"  {e['contenido']}")

# Prueba:
nueva_entrada("Primer día","Hoy empecé el curso de Python. ¡Muy emocionado!")
nueva_entrada("Aprendí funciones","Las funciones def son increíbles para reutilizar código.")
nueva_entrada("Proyecto final","Completé el sistema de registro. ¡Lo logré!")
leer_entradas()
```

## Ejercicio 8.7 — Desafío: Procesador de CSV con módulos

- Lee un archivo CSV de ventas y genera un reporte completo usando os, datetime y manejo de errores.
- El CSV tiene columnas: fecha, vendedor, producto, cantidad, precio_unit.
- Calcula: total por vendedor, total por producto, día más rentable.
- Genera un reporte en un nuevo archivo 'reporte_YYYYMMDD.txt' con la fecha actual en el nombre.
- Si el CSV no existe, créalo con datos de ejemplo antes de procesarlo.

```python
import csv
import os
from datetime import datetime
from collections import defaultdict

ARCHIVO_CSV = 'ventas.csv'

def crear_csv_ejemplo():
    datos = [["fecha","vendedor","producto","cantidad","precio"],
             ["2024-01-15","Ana","Laptop",2,3500],
             ["2024-01-15","Carlos","Mouse",5,85],
             ["2024-01-16","Ana","Teclado",3,220],
             ["2024-01-16","María","Laptop",1,3500],
             ["2024-01-17","Carlos","Monitor",2,1200]]
    with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(datos)
    print("CSV de ejemplo creado.")

def procesar_ventas():
    if not os.path.exists(ARCHIVO_CSV):
        crear_csv_ejemplo()

    por_vendedor = defaultdict(float)
    por_producto = defaultdict(float)
    por_dia      = defaultdict(float)

    try:
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                total = int(fila['cantidad']) * float(fila['precio'])
                por_vendedor[fila['vendedor']] += total
                por_producto[fila['producto']] += total
                por_dia[fila['fecha']]          += total
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Generar reporte
    fecha_hoy = datetime.now().strftime('%Y%m%d')
    reporte   = f'reporte_{fecha_hoy}.txt'

    with open(reporte, 'w', encoding='utf-8') as f:
        f.write("=== REPORTE DE VENTAS ===\n")
        f.write(f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        f.write("Por vendedor:\n")
        for v,t in sorted(por_vendedor.items(), key=lambda x: x[1], reverse=True):
            f.write(f"  {v}: Bs. {t:,.2f}\n")
        f.write(f"\nDía más rentable: {max(por_dia, key=por_dia.get)}\n")

    print(f"Reporte guardado en {reporte}")
    return reporte

procesar_ventas()
```

## Ejercicio 8.8 — Mini proyecto: Gestor de tareas (To-Do List)	

- Crea un gestor de tareas completo con persistencia en JSON.
- Cada tarea tiene: id, titulo, descripcion, estado (pendiente/completada), fecha_creacion, prioridad (alta/media/baja).
- Implementa: agregar_tarea, completar_tarea, listar_tareas (filtrable por estado), eliminar_tarea.
- Todas las operaciones deben tener manejo de errores.
- Usa datetime para las fechas y os para verificar el archivo.

```python
import json, os
from datetime import datetime

ARCHIVO = 'tareas.json'

def cargar(): return json.load(open(ARCHIVO,'r',encoding='utf-8')) if os.path.exists(ARCHIVO) else []
def guardar(t): json.dump(t, open(ARCHIVO,'w',encoding='utf-8'), ensure_ascii=False, indent=4)

def agregar_tarea(titulo, descripcion='', prioridad='media'):
    try:
        if prioridad not in ['alta','media','baja']:
            raise ValueError("Prioridad debe ser: alta, media o baja")
        tareas = cargar()
        nueva = {
            'id':          len(tareas) + 1,
            'titulo':      titulo,
            'descripcion': descripcion,
            'estado':      'pendiente',
            'prioridad':   prioridad,
            'fecha':       datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        tareas.append(nueva)
        guardar(tareas)
        print(f"Tarea #{nueva['id']} agregada.")
    except ValueError as e:
        print(f"Error: {e}")

def completar_tarea(id_tarea):
    tareas = cargar()
    for t in tareas:
        if t['id'] == id_tarea:
            t['estado'] = 'completada'
            guardar(tareas)
            print(f"Tarea #{id_tarea} marcada como completada.")
            return
    print(f"Tarea #{id_tarea} no encontrada.")

def listar_tareas(filtro=None):
    tareas = cargar()
    mostrar = [t for t in tareas if filtro is None or t['estado']==filtro]
    for t in mostrar:
        icono = 'V' if t['estado']=='completada' else 'P'
        prior = t['prioridad'].upper()[:1]
        print(f"[{icono}][{prior}] #{t['id']} {t['titulo']} ({t['fecha']})")

# Prueba:
agregar_tarea('Estudiar Python','Repasar Módulo 8','alta')
agregar_tarea('Hacer ejercicios','Completar todos','media')
agregar_tarea('Presentar proyecto','Demo final','alta')
completar_tarea(1)
listar_tareas()
listar_tareas('pendiente')
```
## Ejercicio 8.9 — Desafío: Sistema de inventario con persistencia completa	

- Extiende el sistema de inventario del Módulo 7 con persistencia en JSON y manejo de errores.
- Agrega las funciones: exportar_txt (genera reporte en texto plano) y cargar_desde_csv.
- Implementa un log de operaciones que registre cada cambio con fecha/hora en 'inventario.log'.
- Valida todos los inputs con try/except antes de modificar el inventario.
- Usa os para verificar existencia de archivos y crear el directorio 'datos/' si no existe.

```python
import json, os, csv
from datetime import datetime

os.makedirs('datos', exist_ok=True)
ARCHIVO_INV  = os.path.join('datos', 'inventario.json')
ARCHIVO_LOG  = os.path.join('datos', 'inventario.log')

def registrar_log(accion, detalle=''):
    ts = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(ARCHIVO_LOG, 'a', encoding='utf-8') as f:
        f.write(f"[{ts}] {accion}: {detalle}\n")

def cargar_inventario():
    try:
        if os.path.exists(ARCHIVO_INV):
            with open(ARCHIVO_INV, 'r', encoding='utf-8') as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        registrar_log("ERROR", f"Al cargar inventario: {e}")
    return {}

def guardar_inventario(inv):
    with open(ARCHIVO_INV, 'w', encoding='utf-8') as f:
        json.dump(inv, f, ensure_ascii=False, indent=4)

def agregar_producto(inv, codigo, nombre, precio, stock):
    try:
        if precio <= 0: raise ValueError('Precio debe ser positivo')
        if stock  < 0:  raise ValueError('Stock no puede ser negativo')
        inv[codigo] = {'nombre':nombre,'precio':precio,'stock':stock}
        guardar_inventario(inv)
        registrar_log("AGREGAR", f"{codigo}: {nombre}")
    except ValueError as e:
        registrar_log("ERROR", str(e))
        print(f"Error: {e}")

def exportar_txt(inv):
    fecha = datetime.now().strftime('%Y%m%d_%H%M')
    archivo = f'datos/reporte_{fecha}.txt'
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write("=== REPORTE DE INVENTARIO ===\n")
        f.write(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        for cod, datos in inv.items():
            f.write(f"{cod}: {datos['nombre']} — Bs.{datos['precio']:,.2f} ({datos['stock']} uds)\n")
        valor_total = sum(d['precio']*d['stock'] for d in inv.values())
        f.write(f"\nValor total inventario: Bs. {valor_total:,.2f}\n")
    print(f"Reporte exportado: {archivo}")

# Prueba:
inv = cargar_inventario()
agregar_producto(inv,"P001","Laptop HP",3500,5)
agregar_producto(inv,"P002","Mouse USB",85,20)
agregar_producto(inv,"P003","Monitor",-100,3)  # ← error: precio negativo
exportar_txt(inv)
```

## Ejercicio 8.10 — PROYECTO FINAL — Sistema de Registro de Estudiantes

- Implementa el sistema completo de registro de estudiantes descrito en el contenido del módulo.
- El sistema debe incluir TODOS los siguientes requisitos:
  - → Menú interactivo con bucle while True y break.
  - → Función agregar_estudiante con validaciones (nombre no vacío, nota 0-100, matrícula única).
  - → Función listar_estudiantes con reporte formateado usando f-strings.
  - → Función calcular_estadisticas (promedio, máx, mín, % aprobados).
  - → Persistencia en JSON (cargar al inicio, guardar en cada modificación).
  - → Manejo de errores en TODAS las funciones con try/except.
  - → Uso de os.path.exists para verificar el archivo al cargar.
  - → Uso de datetime para registrar la fecha de cada registro.
  - → El archivo principal usa if __name__ == '__main__': para llamar a main().
  - → Presentación en vivo de 5 minutos ante el grupo.-
```python
"""
PROYECTO FINAL — Python Básico
Sistema de Registro de Estudiantes

Autor:    ___________________________
Carnet:   ___________________________
Fecha:    ___________________________
"""

import json
import os
from datetime import datetime

ARCHIVO_DATOS   = 'estudiantes.json'
NOTA_APROBACION = 51

# ═══ IMPLEMENTA AQUÍ TUS FUNCIONES ═══

def cargar_datos():
    # TODO: cargar desde JSON con try/except
    pass

def guardar_datos(estudiantes):
    # TODO: guardar a JSON con try/except
    pass

def agregar_estudiante(estudiantes):
    # TODO: pedir datos, validar, agregar y guardar
    pass

def listar_estudiantes(estudiantes):
    # TODO: mostrar todos con formato tabla
    pass

def calcular_estadisticas(estudiantes):
    # TODO: promedio, máx, mín, % aprobados
    pass

def mostrar_menu():
    # TODO: imprimir el menú de opciones
    pass

def main():
    estudiantes = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input('Opción: ').strip()
        if   opcion == "1": agregar_estudiante(estudiantes)
        elif opcion == "2": listar_estudiantes(estudiantes)
        elif opcion == "3": calcular_estadisticas(estudiantes)
        elif opcion == "0": print("¡Hasta luego!"); break
        else: print("Opción inválida.")

if __name__ == "__main__":
    main()

 ```