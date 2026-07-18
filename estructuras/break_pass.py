# impresion de los numeros devisibles entre 7
for n in range(1,17):
  if n%7==0:
    print(n); break # 7

# imprimiendo los numeros impares
for i in range(1,11):
  if i%2==0: continue
  print(i) # 1 3 5 7 9

# obviando al 3
for i in range(5):
  if i==3: pass #algo pero nose que aplicar
  print(i)
