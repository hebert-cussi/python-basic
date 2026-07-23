nums = {0, 1,2,3,2,1,4,3,5,1 }
unicos = {1, 2, 3, 4, 5, 6}

vacio={}

print(f"cantidad datos A: {len(nums)}")
print(f"cantidad datos B: {len(unicos)}")
print(f"cantidad datos C: {len(vacio)}")
print("---------------")
print(f"Union A con B: {nums|unicos} ")
print(f"Interseccion A con B: {nums&unicos} ")
print(f"Diferencia A con B: {nums-unicos} ")
print(f"Diferencia B con A: {unicos-nums} ")
print(f"Diferencia simetrica A con B: {nums^unicos} ")

print("---------------")
print("---------------")

py  = {'Ana','Carlos','María','Luis'}
js  = {'Carlos','Pedro','María','Sofía'}

# Unión
py | js   # todos
# Intersección
py & js   # ambos
# Diferencia
py - js   # solo py

union  = py|js  # {Ana,Carlos,María,Luis,Pedro,Sofía}
ambos  = py&js  # {Carlos, María}
solo_py= py-js  # {Ana, Luis}
solo_js= js-py  # {Ana, Luis}
solo_js_o_py= js^py  # {Ana,Luis,Pedro,Sofía}

print(f" Union : {union}")
print(f" Interseccion : {ambos}")
print(f" Solo Python : {solo_py}")
print(f" Solo Javascript : {solo_js}")
print(f" Diferecia simetrica : {solo_js_o_py}")