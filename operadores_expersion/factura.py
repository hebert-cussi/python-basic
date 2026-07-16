# solicitando el producto
producto = input("Producto:")
# el precio del producto
precio   = float(input("Precio (Bs.): "))
# cantidad del producto
cantidad = int(input("Cantidad: "))
# introduciendo el descuento 
desc     = float(input("Descuento %: "))
# operaciones
subtotal = precio * cantidad
dcto     = subtotal * (desc / 100)
base     = subtotal - dcto
iva      = base * 0.13
total    = base + iva
valida   = cantidad > 0 and precio > 0

print(f"Subtotal: {subtotal}")