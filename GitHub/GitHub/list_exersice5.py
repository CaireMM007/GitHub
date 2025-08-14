otro = []

numeros = input("Ingresa cuantos numeros quiera, solo separalos por coma: ").split(",")

for num in numeros:
    otro.append(int(num))
 
print(otro)
print(f"la suma es: {sum(otro)}")
