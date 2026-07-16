# Calculadora de vuelto
#precio = 37
# pago   = 50

precio = float(input("Digite el precio del producto: "))
pago = float(input("Digite cuanto esa recibiento: "))

# operaciones
vuelto    = pago - precio  # 13
billetes  = vuelto // 10   # 1
monedas   = vuelto % 10    # 3
print(f"Vuelto: Bs. {vuelto}")
print(f" x10: {billetes} suelto: {monedas}")