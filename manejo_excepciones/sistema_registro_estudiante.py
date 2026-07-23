import os
import json
import datetime

ARCHIVO = "estudiante.json"

def guardar_datos(estudiantes):
  print(estudiantes)

def agregar_estudiante(estudiantes):
  try:
    nombre = input('Nombre: ').strip()
    if not nombre: raise ValueError("Nombre vacío")
    mat = input('Matrícula: ').upper()
    if mat in estudiantes: raise ValueError("Ya existe")
    nota = float(input('Nota: '))
    if not 0<=nota<=100: raise ValueError("Nota inválida")
    estudiantes[mat] = {
      'nombre':nombre,
      'nota':nota,
      'estado':'Aprobado' if nota>=51 else 'Reprobado',
      'fecha': datetime.now()}
    guardar_datos(estudiantes)

  except ValueError as error:
    print(f"Error: {error}")

def cargar_datos():
  try:
    if os.path.exists(ARCHIVO):
        json.load(open(ARCHIVO, 'r', encoding='utf-8'))
    return {}
  except FileNotFoundError:
    print('El archivo no existe')

def mostrar_menu():
  print("\n╔══════════════════════════════════╗")
  print("║   📚 Sistema de estuante         ║")
  print("╠══════════════════════════════════╣")
  print("║  1. Registrar estudiante              ║")
  print("║  0. Salir                        ║")
  print("╚══════════════════════════════════╝")

def main():
  estudiantes = cargar_datos()
  while True:
    mostrar_menu()
    op = input('Opción: ')
    if   op=="1": agregar_estudiante(estudiantes)
    elif op=="0":
      print("¡Hasta luego!"); break
    else: print("Inválida")

if __name__=="__main__":
  main()