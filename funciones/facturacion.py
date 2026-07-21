IVA = 0.13  # constante global

# funcion calcular subtotal 
def calcular_subtotal(precio, cantidad):
  return precio * cantidad

# Calculando el descuento
def aplicar_descuento(sub, pct=0):
  desc = sub * (pct/100)
  return sub - desc, desc

# Calcular el IVA
def calcular_iva(base):
  return base * IVA

# Funcion genera factura
def generar_factura(prod, precio, cant, desc=0, aplica_iva=True):
  sub      = calcular_subtotal(precio, cant)
  base, dsc = aplicar_descuento(sub, desc)
  iva      = calcular_iva(base)
  total    = base + iva
  print(f"TOTAL: Bs. {total:.2f}")
  return total

total=0
total+=generar_factura("Cuaderno", 15, 3)
total+=generar_factura("Boligrafos", 1.5,4,5)
#generar_factura("Goma", 2,2)

print(f" El total a pagar es Bs.:{total:.2f}")