"""

Ejercicio 4.2 — Calculadora de tarifa de taxi

–	Solicita los kilómetros recorridos y el horario (día o noche).
–	Calcula la tarifa según estas reglas:
–	  → Tarifa base: Bs. 5.00
–	  → Km diurno (06:00–22:00): Bs. 2.50 por km
–	  → Km nocturno (22:00–06:00): Bs. 3.75 por km (50% adicional)
–	  → Descuento del 10% si el recorrido supera 20 km
–	Muestra el desglose completo de la tarifa.

"""
# Calculadora de tarifa de taxi
km       = float(input("Kilómetros recorridos: "))
horario  = input("Horario (dia/noche): ").lower()

tarifa_base = 5.0

if horario == "dia":
    costo_km = km * 2.50
elif horario == "noche":
    costo_km = km * 3.75 # 50% adicional sobre 2.50 (2.50 * 1.5 = 3.75)
else:
    print("Horario inválido")

subtotal = tarifa_base + costo_km

# Aplica descuento si supera 20 km
if km > 20:
    descuento = subtotal*0.10 # 10% de descuento sobre el subtotal
else:
    descuento = 0

total = subtotal - descuento

print(f"Tarifa base:  Bs. {tarifa_base:.2f}")
print(f"Costo km:     Bs. {costo_km:.2f}")
print(f"Descuento:    Bs. {descuento:.2f}")
print(f"TOTAL:        Bs. {total:.2f}")
