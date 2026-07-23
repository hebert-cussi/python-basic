try:
  with open('notas2.txt','r',encoding='utf-8') as f:
    contenido = f.read()
except FileNotFoundError:
  print('El archivo no existe')
except PermissionError:
  print('Sin permisos para leer')