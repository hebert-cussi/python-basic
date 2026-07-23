inventario = {
  "P001":{
    "nombre":"Laptop",
    "precio":3500,
    "stock":5,
    "cat":"comp"
    },
  "P002":{
    "nombre":"Mouse",
     "precio":85,
     "stock":20,
     "cat":"perf"},
  "P003":{
    "nombre":"Monitor",
    "precio":1200,
    "stock":3,
    "cat":"comp"},
}
# Categorías únicas con set
cats = {p['cat'] for p in inventario.values()}  # {'comp','perf'}

print(f"Categorias: {cats}")

# Agrupar por categoría con dict
por_cat = {}

for cod,datos in inventario.items():
  c = datos['cat']
  por_cat.setdefault(c, [])
  por_cat[c].append(datos['nombre'])
# Total del inventario
total = sum(d['precio']*d['stock'] for d in inventario.values())
print(f"Valor total: Bs. {total:,.2f}")