
total = 0
while True:
  print ("="*15)
  print("1.Cuaderno Bs.15")
  print("2.Lápiz Bs.3.5")
  print("3.Mochila Bs.120")
  print("0.Finalizar")
  print ("="*15)
  op = input("Elige: ")
  if op == "0": break
  elif op == "1": precio=15.0; nom="Cuaderno"
  elif op == "2": precio=3.5; nom="Lápiz"
  elif op == "3": precio=120.0; nom="Mochila"
  else: print("Inválido"); continue
  cant = int(input(f"¿Cuántos {nom}s? "))
  sub = precio * cant; 
  total += sub
  print(f"+ Bs. {sub:.2f}")
print(f"TOTAL: Bs. {total:.2f}")