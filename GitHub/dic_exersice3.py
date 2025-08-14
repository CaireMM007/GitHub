productos = {
    "pan": {"precio": 50, "stock": 15},
    "azucar": {"precio": 100, "stock": 1},
    "banana": {"precio": 60, "stock": 20}           
}

une = productos["pan"].pop("stock")
two = productos["azucar"].pop("stock")
three = productos["banana"].pop("stock")
"""
pres1 = productos["pan"].pop("precio")
pres2 = productos["azucar"].pop("precio")
pres3 = productos["banana"].pop("precio")
"""

for key, value in productos.items():
    print(key, value)

for _ in range(1000):
    user = input("Elije un producto de la lista: ").lower()
    match user:
        case "pan": 
            while une != 0:
                print("su precio es de 50$, Gracias por comprar con nosotros")
                une -= 1
                break
            else:
                print("lo sentimos, no quedan productos")
        case "azucar":
            while two != 0:
                print("su precion es de 100$, Gracias por comprar con nosotros")
                two -= 1
                break
            else:
                print("lo sentimos, no quedan productos")
        case "banana":
            while three != 0:
                print("su precion es de 60$, Gracias por comprar con nosotros")
                three -= 1
                break
            else:
                print("lo sentimos, no quedan productos")
        case _:
            print("Escribe un producto de la lista")

    desicion = input("Desea volver a comprar? (Yes/No): ").lower()

    if desicion == "si" or desicion == "yes":
        continue
    else:
        print("Gacias por comprar con tienda 'CaireMM'")
        break