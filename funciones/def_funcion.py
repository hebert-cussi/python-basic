def sumar(a, b):
  return a + b  # devuelve

def estadisticas(nums):
  return sum(nums), sum(nums)/len(nums), max(nums), min(nums)  # retorna una tupla


def saludar(nombre, cargo):
    print(f"Hola {nombre} ({cargo})")

def calcular_iva(precio, tasa=0.13):
    return precio * tasa

def pedido(producto, cantidad, precio):
    print(f"{cantidad}x {producto} = Bs. {cantidad*precio:.2f}")

# 1. DEFINICIÓN (solo define, no ejecuta)
def mostrar_menu(): # DEFINIR LA FUNCION
    print("=" * 25)
    print(" MENÚ DEL SISTEMA")
    print("1. Ingresar datos")
    print("2. Ver reporte")
    print("=" * 25)

# 2. LLAMADA (aquí sí se ejecuta)
mostrar_menu()   # primera vez
# mostrar_menu()   # reutilización
# mostrar_menu()

saludar("Hebert Cussi", "Docente")
print(f"\n")
iva = calcular_iva(100)
print(f"El impuesto a pagar es:Bs. {iva:.2f}")

iue = calcular_iva(100, 0.25)
print(f"El impuesto a pagar a las Utilidades IUE:Bs. {iue:.2f}")

it = calcular_iva(100, 0.03)
print(f"El impuesto a las transacciones (IT)  es :Bs. {it:.2f}")

print(f"\n")
pedido("Cuaderno", 3, 15.0)
pedido( precio= 1.5, cantidad=12, producto="Boligrafos")
# pedido(15,10,"UHU") #Error

#aplica la funacion definida sumar
r = sumar(3, 4)   # r = 7
print(f"La suma de 3 y 4 es: {r:.2f}")
print(f"La mutiplicacion por 2 de la suma de 3 y 4 es: {r*2:.2f}")


total, prom, mx, mn = estadisticas([85, 92, 78, 95])  # desempaquetado

print(f"La suma es: {total:.2f}")
print(f"La promedio es: {prom:.2f}")
print(f"La maximo es: {mx:.2f}")
print(f"La minimo es: {mn:.2f}")



def calcular_impositiva(precio, tasa=13):
    """
    Calcula el impuesto a pagar de un precio.
    Args:
        precio (float): Precio original en Bs.
        tasa (float): % de cobro de impuesto. Def. 13% porcenta de iva.
    Returns:
        float: Impuesto a pagar.
    Ejemplo:
        >>> calcular_impositiva(100, 3)
        3
    """
    return precio * tasa/100

calcular_impositiva()

