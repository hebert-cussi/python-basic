# Tupla — datos fijos del curso
CURSO = ("Python Básico", "2026")
# Listas — datos que cambian
alumnos = ["Ana","Carlos","María","Luis","Marco"]
notas   = [85, 62, 91, 74]
alumnos.append("Sofia"); 
notas.append(88)
# Ranking (zip + sort)
"El objeto `zip` genera tuplas de longitud *n*, "
"donde *n* es el número de iterables pasados ​​como argumentos posicionales "
"a `zip()`."
"El *i*-ésimo elemento de cada tupla proviene del *i*-ésimo argumento iterable de `zip()`. "
"Este proceso continúa hasta que se agota el argumento más corto."
"""
         [ 0, 1 ,2 ,3,5]
alumnos = ["Ana","Carlos","María","Luis","Marco"]
notas   = [85, 62, 91, 74]
          [0, 1, 2, 3]
"""

"""
         [ 0, 1 ,2 ,3, 5, 6]
alumnos = ["Ana","Carlos","María","Luis","Marco", "Sofia"]
notas   = [85, 62, 91, 74,88]
          [0, 1, 2, 3,5 ]

[ ["Ana", 85],
 ["Carlos", 62],
 ["María", 91],
 ["Luis", 74],
 ["Marco" 88 ]]
"""

pares = list(zip(notas, alumnos))
pares.sort(reverse=True)
print(f"=== {CURSO[0]} — Ranking ===")
for pos,(nota,nombre) in enumerate(pares,1):
  est='Aprobado' if nota>=51 else 'Reprobado'
  print(f"{pos}. {nombre:<10} {nota}/100 {est}")
solo_notas = [p[0] for p in pares]
print(f"Top 3: {solo_notas[:3]}")
