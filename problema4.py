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

operaciones = {
    's': suma,
    'r': resta,
    'm': multiplicacion,
    'd': division
}

operacion = input("Elige qué operación quieres hacer (S, R, M, D): ").lower()
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 < 0 or num2 < 0:
    print("Números inválidos")
else:
    if operacion in operaciones:
        resultado = operaciones[operacion](num1, num2)
        print("Tu resultado es:", resultado)
    else:
        print("Operación no válida")