
# escribiendo un archivo .txt
with open('notas.csv','w',encoding='utf-8') as f:
  f.write("Ana López,88.5\n")
  f.write("Carlos Ramos,72.0\n")

with open('notas.txt','a',encoding='utf-8') as f:
  f.write("María Quispe,95.0\n")

# LEER línea por línea
with open('notas.txt','r',encoding='utf-8') as f:
  for linea in f:
    linea = linea.strip()
    nombre, nota = linea.split(',')
    print(f"{nombre}: {nota}")