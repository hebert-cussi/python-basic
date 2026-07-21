empresa="TechBolivia"
empleados=0
def motrar_info():
  #global empleados
  empleados=25
  print(empresa)
  # print(empleados)
  return empleados

empleados=motrar_info()
print(empresa)
print(empleados)

# ***************************
contador = 5

def incrementar():
    global contador
    contador += 1

incrementar()

# print(contador)  # 1