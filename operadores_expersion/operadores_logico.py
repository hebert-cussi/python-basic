# asignacion de valores
edad=22
tiene_carnet=True
saldo=150
# utilizacion de los operador logicos
puede_votar   = edad >= 18 and tiene_carnet  # True (ambas True)
puede_pagar   = saldo >= 200 or tiene_carnet  # True (una es True)
no_tiene_doc  = not tiene_carnet             # False (invierte True)

print(f"->{puede_pagar}")
print(f"->{puede_votar}")
print(f"->{no_tiene_doc}")


-(-1)+5*15