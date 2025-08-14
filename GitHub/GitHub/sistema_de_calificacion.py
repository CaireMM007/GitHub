def prueba(*args):
    numero = sum(args) / len(args) 
    if numero >= 60:
        return f"Aprobaste tu Nota: {numero}"
    elif numero < 60:
        return f"Desaprovaste, tu Nota: {numero}"
    return "Valor NO valido"

print(prueba(50, 40, 90))