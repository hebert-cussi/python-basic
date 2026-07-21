""" frutas = ['manzana','banana','naranja']
for i in range(len(frutas)):
  print(f"{i}: {frutas[i]}") """

# Con enumerate — Pythónico ✅
""" frutas = ['manzana','banana','naranja']
for i, fruta in enumerate(frutas, start=1):
  print(f"{i}: {fruta}") """  

# Acumular resultados con for
precios = [150.0, 45.5, 320.0, 89.0, 210.0]
total=0  
caros=0  
baratos=[]
for i, precio in enumerate(precios, 1):
  # total += precio
  if precio > 100:   caros += 1
  else: baratos.append(precio)
print(precios)
print(f"Total: Bs.{sum(precios):.2f}  Caros: {caros}  Baratos: {baratos}")