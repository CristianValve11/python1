# Pedir nombre y mostrarlo por la pantalla
nombre = input("Introduce tu nombre: ")
print("¡Hola" + nombre)
print("Me alegro de conocerle," + nombre)



nombre = input("Introduce tu nombre: ")
nombreMayus = nombre.upper() #upper para ponerlo en Mayusculas
numeroLetras = len(nombre) #len da la longitud de ka cadena intrducida

print(f"Tu nombre es: {nombreMayus}")
print(f"Número de caracteres: {numeroLetras}")

# Se repite nombre en bucle
#segun número de letras (for each)
for i in range(numeroLetras):
    print(nombre)