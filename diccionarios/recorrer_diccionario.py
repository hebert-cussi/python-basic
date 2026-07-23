precios = {
    'Laptop':3500.0,
    'Mouse':85.0, 
    'Teclado':220.0
    }

for producto in precios:
  print(producto)

for precio in precios.values():
  print(f'Bs. {precio:.2f}')

for prod, precio in precios.items():
  print(f'{prod}: Bs. {precio}')

empleados ={
  "EMP001": {
    "nombre": "Ana López",
    "cargo":  "Desarrolladora",
    "salario": 4500.0,
  },
  "EMP002": {
      "nombre": "Carlos Ramos",
      "cargo":  "Dieseñador",
      "salario": 3800.0
  }
}
print("------------ datos de diccionario")
print(empleados)
print("------------")
print(f"Nombre del empleado: {empleados["EMP001"]["nombre"]}")

print(f"salario {empleados["EMP001"]["salario"]}")