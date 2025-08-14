def pares(num1, num2):
    if num1 < num2:
        for n in range(num1, num2):
            if n % 2 == 0:
                print(n)
            else:
                continue
    else:
        print("orden erroneo de numeros")

pares(0, 10 + 1)