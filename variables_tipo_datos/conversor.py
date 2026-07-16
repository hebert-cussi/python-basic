celcius=int(input("Introduzca cuantos grados celcius quiere convertir? "))

fahreneit =float((celcius*9/5)+32)
kelvin=float(celcius+273.15)

print("Grados Celcius: ",celcius )
print("Grados Fahrenheit: ", round(fahreneit,2) )
print("Grados Kelvin: ", round(kelvin,2) )

print(f"Grados Kelvin: {kelvin:.2f}",  )
