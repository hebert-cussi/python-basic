
# PROYECTOS FINALES

## 0. INSTRUCCIONES GENERALES
Elige UNA de las dos opciones y completa el esqueleto de código. Cada función tiene un bloque # TODO que describe exactamente qué debes implementar. NO modifiques los nombres de las funciones ni la estructura del menú.

Requisitos obligatorios para AMBAS opciones:
- Menú interactivo con bucle while True y break para salir.
- Mínimo 5 funciones propias, cada una con su docstring completo.
- Manejo de errores con try/except en TODAS las funciones que pidan datos al usuario.
- Persistencia: guardar y cargar datos desde un archivo JSON.
- Verificar existencia del archivo con os.path.exists() antes de leerlo.
- Registrar fecha/hora de cada operación usando datetime.
- Usar correctamente al menos dos estructuras de datos (lista, diccionario, conjunto o tupla).
- El archivo principal debe terminar con if __name__ == '__main__': main().
- Presentación oral de 5 minutos con demostración en vivo del programa funcionando.

> ⚠️ **Importante**: No se aceptan proyectos copiados del ejemplo del Módulo 8. El esqueleto es una guía — el código que completes debe ser tuyo.
## OPCIÓN A
### Sistema de Gestión de Biblioteca Personal

#### A.1. DESCRIPCIÓN
Sistema para gestionar una colección personal de libros. Permite registrar libros, marcarlos como leídos, buscar por distintos criterios y ver estadísticas de la biblioteca.

#### A.2. FUNCIONALIDADES A IMPLEMENTAR
|Función|Qué debe hacer|
|-----------|--------|
|registrar_libro()|Solicitar título, autor, género, año. Validar que no estén vacíos y que el año sea válido. |Guardar en el diccionario con clave auto-generada y fecha de registro.|
|listar_libros()|Mostrar todos los libros en formato de tabla. Aceptar parámetro opcional filtro_estado para mostrar solo 'leido' o 'pendiente'.|
|marcar_leido()|Pedir código del libro. Verificar que exista y no esté ya leído. Solicitar calificación 1-5. Actualizar estado y fecha de lectura.|
|buscar_libros()|Ofrecer búsqueda por: 1) título, 2) autor, 3) género. Mostrar resultados que contengan el término |buscado (parcial, sin mayúsculas).|
|estadisticas()|Calcular y mostrar: total, % leídos, promedio de calificaciones, género más leído, conjunto de géneros únicos.|
|eliminar_libro()|Pedir código del libro. Confirmar con s/n. Eliminar y guardar si el usuario confirma.|

#### A.3. ESTRUCTURAS DE DATOS REQUERIDAS
**Diccionario principal (biblioteca):** 
```text
# Cada libro es un diccionario. La clave es el código auto-generado.
biblioteca = {
    "LIB0001": {
        "titulo":        "El Alquimista",
        "autor":         "Paulo Coelho",
        "genero":        "Novela",
        "anio":          1988,
        "estado":        "pendiente",   # o "leido"
        "calificacion":  None,          # int 1-5 cuando se lea
        "fecha_lectura": None,          # str cuando se lea
        "fecha_registro":"15/07/2024 19:30"
    }
}
```
**Otras estructuras que debes usar:**
- Conjunto (set): para obtener los géneros únicos de la biblioteca.
- Lista: para filtrar libros pendientes o resultados de búsqueda.

#### A.4. ESQUELETO DE CÓDIGO — OPCIÓN A
Completa cada bloque marcado con # TODO. No cambies la firma (nombre y parámetros) de las funciones.

```python
"""
Sistema de Gestión de Biblioteca Personal
Proyecto Final — Python Básico

Autor: ___________________________
Fecha: ___________________________
"""

import json
import os
from datetime import datetime

# ═══ CONFIGURACIÓN ═══
ARCHIVO_DATOS = "biblioteca.json"

# ═══ PERSISTENCIA ═══

def cargar_biblioteca():
    """Carga los libros guardados desde el archivo JSON.
    Retorna un diccionario vacío si el archivo no existe.
    """
    # TODO: Verificar si el archivo existe con os.path.exists()
    # TODO: Si existe, abrirlo con open() y cargar con json.load()
    # TODO: Capturar json.JSONDecodeError e IOError con try/except
    # TODO: Si no existe o hay error, retornar {}
    pass


def guardar_biblioteca(biblioteca):
    """Guarda el diccionario de libros en el archivo JSON."""
    # TODO: Abrir el archivo en modo escritura con encoding='utf-8'
    # TODO: Usar json.dump() con indent=4 y ensure_ascii=False
    # TODO: Capturar IOError con try/except y mostrar el error
    pass


# ═══ FUNCIONES DE NEGOCIO ═══

def generar_codigo(biblioteca):
    """Genera un código único tipo LIB0001, LIB0002, etc."""
    # TODO: Retornar f'LIB{len(biblioteca)+1:04d}'
    pass


def registrar_libro(biblioteca):
    """Registra un nuevo libro en la biblioteca con validaciones."""
    print("\n--- REGISTRAR LIBRO ---")
    try:
        # TODO: Pedir título con input() y validar que no esté vacío
        #       Si está vacío, lanzar ValueError('El título no puede estar vacío')
        titulo = ___________

        # TODO: Pedir autor y validar que no esté vacío
        autor = ___________

        # TODO: Pedir género (Novela / Ciencia / Historia / Otro)
        genero = ___________

        # TODO: Pedir año, convertir a int, validar rango 1000 - año actual
        #       Usar datetime.now().year para obtener el año actual
        anio = ___________

        # TODO: Generar código con generar_codigo(biblioteca)
        codigo = ___________

        # TODO: Crear el diccionario del libro con todos los campos:
        #   titulo, autor, genero, anio, estado='pendiente',
        #   calificacion=None, fecha_lectura=None,
        #   fecha_registro = datetime.now().strftime('%d/%m/%Y %H:%M')
        biblioteca[codigo] = {
            ___________
        }

        # TODO: Llamar a guardar_biblioteca(biblioteca)
        # TODO: Mostrar mensaje de éxito con el código generado

    except ValueError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def listar_libros(biblioteca, filtro_estado=None):
    """Muestra todos los libros o filtrados por estado (leido/pendiente)."""
    # TODO: Si biblioteca está vacío, mostrar 'La biblioteca está vacía.' y retornar

    # TODO: Filtrar libros según filtro_estado (si es None, mostrar todos)
    libros = ___________

    # TODO: Si no hay libros con ese filtro, mostrar mensaje y retornar

    # TODO: Imprimir encabezado de tabla con separadores
    # Columnas: Cód | Título | Autor | Año | Estado | Calificación

    # TODO: Iterar sobre libros e imprimir cada fila formateada con f-strings
    #       Si calificacion no es None, mostrar el número + '★', si no '—'
    for cod, libro in libros:
        ___________


def marcar_leido(biblioteca):
    """Marca un libro como leído y registra la calificación."""
    print("\n--- MARCAR COMO LEÍDO ---")
    try:
        # TODO: Pedir código con input() y convertir a mayúsculas
        codigo = ___________

        # TODO: Verificar que el código existe en biblioteca
        #       Si no existe, lanzar KeyError con mensaje claro

        # TODO: Verificar que el estado no sea ya 'leido'
        #       Si ya está leído, mostrar mensaje y retornar

        # TODO: Pedir calificación, convertir a int, validar 1-5
        cal = ___________

        # TODO: Actualizar estado, calificacion y fecha_lectura del libro
        biblioteca[codigo][___________] = ___________
        biblioteca[codigo][___________] = ___________
        biblioteca[codigo][___________] = datetime.now().strftime('%d/%m/%Y')

        # TODO: Guardar y mostrar mensaje de éxito

    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def buscar_libros(biblioteca):
    """Busca libros por título, autor o género (coincidencia parcial)."""
    print("\n--- BUSCAR LIBROS ---")
    print("1. Por título   2. Por autor   3. Por género")
    criterio = input('Criterio (1/2/3): ').strip()

    # TODO: Crear dict que mapee criterio a nombre del campo
    #       {'1': 'titulo', '2': 'autor', '3': 'genero'}
    campos = ___________

    # TODO: Validar que criterio esté en campos, si no mostrar error y retornar

    # TODO: Pedir el término de búsqueda al usuario
    termino = ___________

    # TODO: Filtrar biblioteca: incluir libros donde termino.lower()
    #       esté contenido en el valor del campo correspondiente en minúsculas
    resultados = ___________

    # TODO: Si hay resultados, llamar a listar_libros(resultados)
    #       Si no, mostrar mensaje de 'No se encontraron resultados'


def estadisticas(biblioteca):
    """Muestra estadísticas generales de la biblioteca."""
    # TODO: Si biblioteca está vacío, mostrar mensaje y retornar

    # TODO: Calcular total de libros
    total = ___________

    # TODO: Filtrar los libros con estado 'leido' en una lista
    leidos = ___________

    # TODO: Usar un conjunto (set) para obtener géneros únicos
    generos_unicos = ___________

    # TODO: Calcular calificación promedio (solo libros con calificacion != None)
    #       Si no hay calificaciones, promedio = 0
    prom_cal = ___________

    # TODO: Encontrar el género más leído usando un diccionario contador
    gen_top = ___________

    # TODO: Mostrar todas las estadísticas con f-strings
    print(f"\n--- ESTADÍSTICAS ---")
    ___________


def eliminar_libro(biblioteca):
    """Elimina un libro con confirmación previa del usuario."""
    print("\n--- ELIMINAR LIBRO ---")
    try:
        # TODO: Pedir código y verificar que existe
        codigo = ___________

        # TODO: Mostrar el título del libro y pedir confirmación s/n
        conf = ___________

        # TODO: Si confirma con 's', eliminar con del y guardar
        #       Si no, mostrar 'Operación cancelada.'

    except KeyError as e:
        print(f"Error: {e}")


# ═══ MENÚ PRINCIPAL ═══

def mostrar_menu():
    """Muestra el menú de opciones del sistema."""
    # TODO: Imprimir el menú con las 7 opciones + opción 0 para salir
    # Opciones: 1.Registrar, 2.Ver todos, 3.Ver pendientes,
    #           4.Marcar leído, 5.Buscar, 6.Estadísticas, 7.Eliminar, 0.Salir
    pass


def main():
    """Función principal — carga datos e inicia el bucle del menú."""
    biblioteca = cargar_biblioteca()
    print(f"Biblioteca cargada: {len(biblioteca)} libro(s).")

    while True:
        mostrar_menu()
        op = input('Selecciona una opción: ').strip()

        if   op == "1": registrar_libro(biblioteca)
        elif op == "2": listar_libros(biblioteca)
        elif op == "3": listar_libros(biblioteca, "pendiente")
        elif op == "4": marcar_leido(biblioteca)
        elif op == "5": buscar_libros(biblioteca)
        elif op == "6": estadisticas(biblioteca)
        elif op == "7": eliminar_libro(biblioteca)
        elif op == "0":
            print("¡Hasta luego!")
            break
        else: print("Opción inválida.")


if __name__ == "__main__":
    main()
```
💡 **Tip:** Guarda este archivo como 'biblioteca.py'. Implementa primero cargar_biblioteca() y guardar_biblioteca(), luego registrar_libro(). Prueba cada función antes de seguir con la siguiente.
## OPCIÓN B
### Sistema de Control de Gastos Personales

#### B.1. DESCRIPCIÓN
Sistema para registrar y analizar gastos personales mensuales. Permite ingresar gastos por categoría, establecer presupuestos, ver resúmenes con alertas y exportar reportes a un archivo de texto.

#### B.2. FUNCIONALIDADES A IMPLEMENTAR
|Función|Qué debe hacer|
|--------|------|
|**registrar_gasto()**|Solicitar descripción, monto (> 0) y categoría. Crear dict del gasto con id auto-incremental, fecha automática y mes en formato YYYY-MM. Agregar a la lista y guardar.|
|**listar_gastos()**|Mostrar gastos en tabla. Aceptar filtros opcionales: categoria y mes. Mostrar total al pie de la tabla.|
|**establecer_presupuesto()**|Pedir categoría y monto límite mensual (> 0). Guardar en el diccionario de presupuestos. Persistir en JSON.|
|**resumen_mensual()**|Agrupar gastos del mes actual por categoría. Comparar con presupuestos. Mostrar alerta ⚠️ EXCEDIDO si se superó el límite. Mostrar total del mes.|
|**exportar_resumen()**|Generar archivo 'resumen_YYYY-MM.txt' con el resumen del mes: total por categoría y total general, con fecha de generación.|

#### B.3. ESTRUCTURAS DE DATOS REQUERIDAS
Lista de gastos (cada gasto es un diccionario):
# Los gastos se almacenan en una lista de diccionarios
```text
gastos = [
    {
        "id":          1,
        "descripcion": "Almuerzo en restaurante",
        "monto":       45.50,
        "categoria":   "Alimentación",
        "fecha":       "15/07/2024",
        "mes":         "2024-07"
    },
    # ... más gastos
]
```
**Otras estructuras que debes usar:**
- Diccionario de presupuestos: clave = categoría, valor = monto límite mensual.
- Tupla de categorías predefinidas: inmutable, definida como constante global.
- Conjunto (set): para obtener las categorías únicas que tienen gastos registrados.

**Categorías predefinidas (usar como tupla):**
```texto
CATEGORIAS = ('Alimentación', 'Transporte', 'Salud', 'Educación',
              'Entretenimiento', 'Ropa', 'Hogar', 'Otros')
```

#### B.4. ESQUELETO DE CÓDIGO — OPCIÓN B
Completa cada bloque marcado con # TODO. No cambies la firma (nombre y parámetros) de las funciones.

```python
"""
Sistema de Control de Gastos Personales
Proyecto Final — Python Básico

Autor: ___________________________
Fecha: ___________________________
"""

import json
import os
from datetime import datetime

# ═══ CONFIGURACIÓN ═══
ARCHIVO_GASTOS       = "gastos.json"
ARCHIVO_PRESUPUESTOS = "presupuestos.json"
CATEGORIAS = ('Alimentación', 'Transporte', 'Salud', 'Educación',
              'Entretenimiento', 'Ropa', 'Hogar', 'Otros')


# ═══ PERSISTENCIA ═══

def cargar_json(archivo, tipo_vacio):
    """Carga datos desde un archivo JSON.
    tipo_vacio: [] para listas, {} para diccionarios.
    """
    # TODO: Verificar si el archivo existe con os.path.exists()
    # TODO: Si existe, abrir y cargar con json.load() dentro de try/except
    # TODO: Capturar json.JSONDecodeError e IOError
    # TODO: Retornar tipo_vacio si el archivo no existe o hay error
    pass


def guardar_json(datos, archivo):
    """Guarda los datos en un archivo JSON con formato legible."""
    # TODO: Abrir archivo en modo escritura con encoding='utf-8'
    # TODO: Usar json.dump() con ensure_ascii=False e indent=4
    # TODO: Capturar IOError con try/except
    pass


# ═══ FUNCIONES AUXILIARES ═══

def mostrar_categorias():
    """Imprime la lista numerada de categorías disponibles."""
    # TODO: Usar enumerate(CATEGORIAS, 1) para imprimir numeradas
    pass


def seleccionar_categoria():
    """Solicita al usuario elegir una categoría válida. Retorna el nombre."""
    mostrar_categorias()
    while True:
        try:
            # TODO: Pedir número, convertir a int, validar rango 1 a len(CATEGORIAS)
            # TODO: Retornar CATEGORIAS[op - 1]
            # TODO: Si ValueError o fuera de rango, mostrar error y repetir
            op = ___________
            ___________
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intenta de nuevo.")


# ═══ FUNCIONES DE NEGOCIO ═══

def registrar_gasto(gastos):
    """Registra un nuevo gasto con validación completa."""
    print("\n--- REGISTRAR GASTO ---")
    try:
        # TODO: Pedir descripción y validar que no esté vacía
        desc = ___________

        # TODO: Pedir monto, convertir a float, validar que sea > 0
        monto = ___________

        # TODO: Mostrar mensaje y llamar a seleccionar_categoria()
        categoria = ___________

        # TODO: Crear el diccionario del gasto con los campos:
        #   id = len(gastos) + 1
        #   descripcion, monto = round(monto, 2), categoria
        #   fecha = datetime.now().strftime('%d/%m/%Y')
        #   mes   = datetime.now().strftime('%Y-%m')
        gasto = {
            ___________
        }

        # TODO: Agregar gasto a la lista con append()
        # TODO: Guardar con guardar_json(gastos, ARCHIVO_GASTOS)
        # TODO: Mostrar mensaje de éxito con monto y categoría

    except ValueError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def listar_gastos(gastos, categoria=None, mes=None):
    """Lista gastos con filtros opcionales de categoría y mes."""
    # TODO: Filtrar la lista de gastos según categoria y mes
    #       Si ambos son None, mostrar todos
    filtrados = ___________

    # TODO: Si no hay gastos filtrados, mostrar mensaje y retornar

    # TODO: Imprimir encabezado de tabla
    # Columnas: # | Descripción | Categoría | Monto | Fecha

    # TODO: Iterar e imprimir cada gasto con f-strings y formato
    for g in filtrados:
        ___________

    # TODO: Mostrar el total sumando todos los montos de filtrados
    print(f"TOTAL: Bs. {___________:,.2f}")


def establecer_presupuesto(presupuestos):
    """Establece o actualiza el presupuesto mensual de una categoría."""
    print("\n--- ESTABLECER PRESUPUESTO ---")
    # TODO: Llamar a seleccionar_categoria() para obtener la categoría
    categoria = ___________
    try:
        # TODO: Pedir monto límite, convertir a float, validar > 0
        monto = ___________

        # TODO: Guardar presupuestos[categoria] = round(monto, 2)
        # TODO: Llamar a guardar_json(presupuestos, ARCHIVO_PRESUPUESTOS)
        # TODO: Mostrar mensaje de confirmación

    except ValueError as e:
        print(f"Error: {e}")


def resumen_mensual(gastos, presupuestos):
    """Muestra el resumen del mes actual con alertas de presupuesto."""
    # TODO: Obtener el mes actual con datetime.now().strftime('%Y-%m')
    mes_actual = ___________

    # TODO: Filtrar gastos del mes actual
    gastos_mes = ___________

    # TODO: Si no hay gastos, mostrar mensaje y retornar

    # TODO: Agrupar montos por categoría en un diccionario
    #       por_cat = {}  → por_cat[categoria] += monto
    por_cat = {}
    for g in gastos_mes:
        ___________

    # TODO: Calcular total del mes
    total_mes = ___________

    # TODO: Imprimir encabezado del resumen con el mes actual

    # TODO: Iterar sobre por_cat.items() y para cada categoría:
    #   - Obtener presupuesto con presupuestos.get(cat, None)
    #   - Si tiene presupuesto: calcular % usado y mostrar alerta si excedió
    #   - Si no tiene presupuesto: mostrar 'Sin límite'
    for cat, gastado in sorted(por_cat.items(), key=lambda x: x[1], reverse=True):
        presp = ___________
        ___________

    # TODO: Mostrar total del mes al final


def exportar_resumen(gastos, presupuestos):
    """Exporta el resumen mensual a un archivo de texto."""
    mes_actual  = datetime.now().strftime('%Y-%m')
    # TODO: Filtrar gastos del mes actual
    gastos_mes  = ___________

    # TODO: Si no hay datos, mostrar mensaje y retornar

    # TODO: Agrupar por categoría igual que en resumen_mensual()
    por_cat = {}
    ___________

    # TODO: Generar nombre de archivo: f'resumen_{mes_actual}.txt'
    nombre_arch = ___________

    # TODO: Abrir el archivo en modo escritura con encoding='utf-8'
    # TODO: Escribir: título, fecha de generación, cada categoría con total
    #       y el total general al final
    with open(nombre_arch, 'w', encoding='utf-8') as f:
        ___________

    # TODO: Mostrar mensaje indicando el nombre del archivo generado


# ═══ MENÚ PRINCIPAL ═══

def mostrar_menu():
    """Muestra el menú de opciones del sistema."""
    # TODO: Imprimir el menú con las 6 opciones + opción 0 para salir
    # Opciones: 1.Registrar gasto, 2.Ver gastos, 3.Filtrar por categoría,
    #           4.Establecer presupuesto, 5.Resumen mensual,
    #           6.Exportar resumen, 0.Salir
    pass


def main():
    """Función principal — carga datos e inicia el bucle del menú."""
    gastos       = cargar_json(ARCHIVO_GASTOS, [])
    presupuestos = cargar_json(ARCHIVO_PRESUPUESTOS, {})
    print(f"Sistema de Gastos iniciado. {len(gastos)} gasto(s) cargado(s).")

    while True:
        mostrar_menu()
        op = input('Selecciona una opción: ').strip()

        if   op == "1": registrar_gasto(gastos)
        elif op == "2": listar_gastos(gastos)
        elif op == "3":
            print("Selecciona categoría a filtrar:")
            cat = seleccionar_categoria()
            listar_gastos(gastos, categoria=cat)
        elif op == "4": establecer_presupuesto(presupuestos)
        elif op == "5": resumen_mensual(gastos, presupuestos)
        elif op == "6": exportar_resumen(gastos, presupuestos)
        elif op == "0":
            print("¡Hasta luego!")
            break
        else: print("Opción inválida.")


if __name__ == "__main__":
    main()
```
>💡 **Tip:* Guarda este archivo como 'gastos.py'. Implementa primero cargar_json() y guardar_json(), luego registrar_gasto(). Prueba cada función por separado antes de continuar.
 #### C. RÚBRICA DE EVALUACIÓN (aplica a ambas opciones)

|Criterio de Evaluación	|Puntaje|
|:-------|----:|
|**Funcionalidad** El programa corre sin errores y cumple todos los requisitos funcionales|30%|
|**Manejo de errores** try/except en todas las entradas del usuario y operaciones de archivo|15%|
|**Persistencia** Datos se guardan y cargan correctamente desde JSON|15%|
|**Calidad del código** Funciones con docstrings, nombres claros, indentación correcta, PEP 8|15%|
|**Uso de estructuras** Uso adecuado de listas, diccionarios, conjuntos y/o tuplas	10%|
|**Presentación oral** Explicación clara de 5 min: ¿qué hace?, ¿cómo?, demostración en vivo|15%|
|**TOTAL**|100%|

#### D. GUÍA DE PRESENTACIÓN — 5 minutos
Estructura sugerida:
-	0:00 – 0:30  Introducción: tu nombre, la opción elegida y para qué sirve el programa.
-	0:30 – 2:00  Demostración en vivo: ejecutar el programa y mostrar al menos 3 funcionalidades.
-	2:00 – 3:00  Explicación técnica: ¿qué estructuras de datos usaste y por qué las elegiste?
-	3:00 – 4:00  Manejo de errores: ingresar un dato inválido a propósito y mostrar cómo reacciona el programa.
-	4:00 – 5:00  Persistencia: cerrar el programa, volver a abrirlo y mostrar que los datos siguen guardados.

> ⚠️ **Importante:** El programa debe estar ejecutándose correctamente en tu computadora ANTES de que empiece tu turno. No habrá tiempo para corregir errores durante la presentación.

>📝 **TODO:** Antes de la presentación verifica: ✓ El programa corre sin errores  ✓ Los datos se guardan en JSON  ✓ Los errores se manejan correctamente  ✓ Tienes al menos 3 registros de prueba cargados

Documento confidencial – Uso exclusivo académico - Lic. Hebert E. Cussi Cuentas
