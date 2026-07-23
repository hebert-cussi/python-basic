alumno = {
  "nombre": "Ana López",
  "edad":    22,
  "ciudad": "La Paz",
  "activo":  True,
  "promedio":88.5
}

# Acceder
print(alumno["nombre"])
#print(alumno["tel"])
print(alumno.get('tel','N/A'))

print(alumno)
# Acceder
alumno["nombre"]         # "Ana" ✅
# alumno["telefono"]       # KeyError ❌
alumno.get("telefono")  # None ✅
alumno.get("tel", "N/A") # "N/A" ✅

# Agregar / modificar
alumno["carrera"] = "Ingeniería"
alumno["edad"]    = 23

print("----------------")
print(alumno)

# Eliminar
del alumno["activo"]    # elimina
v = alumno.pop("ciudad")  # elim.+retorna
print(v)
v = alumno.pop("x", None) # sin KeyError
print(v)
print("----------------")
print(alumno)

# Verificar existencia
valor= "nombre" in alumno  # True

print(valor)