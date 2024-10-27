limiteDeNumero = int(input("Introduce un número: "))
print("Números pares desde 2 hasta", limiteDeNumero)
#con un buccle foreach, recorremos todas las impresiones, de 2 en 2, empezando por el 2
for i in range(2, limiteDeNumero + 1, 2):
    print(i)