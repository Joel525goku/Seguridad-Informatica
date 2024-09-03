def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Operaciones básicas en Python")

    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))

    print(f"Suma: {suma(x, y)}")
    print(f"Resta: {resta(x, y)}")
    print(f"Multiplicación: {multiplicacion(x, y)}")

    resultado_division = division(x, y)
    print(f"División: {resultado_division}")


if __name__ == "__main__":
    main()


