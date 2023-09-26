# Calculadora de IMC
# IMC = Peso / (Altura * Altura)
# < 19: Delgado
# Entre 20 y 25: Normal
# Entre 26 y 30: Sobrepeso
# > 30: Obesidad

contador = 0

# Función para calcular el índice de masa corporal


def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

# Función que pide al usuario los datos para realizar el calculo


def pedirIMC():
    peso = float(input('Ingrese su peso en kg: '))
    alturaEnCM = int(input('Ingrese su altura en cm: '))
    alturaEnMetros = alturaEnCM / 100
    imc = calcularIMC(peso, alturaEnMetros)

    print('Su IMC es de: ' + str(imc))

    if imc < 20:
        print('Estado de delgadez')
    if 20 <= imc < 26:
        print('Estado normal')
    if 26 <= imc < 30:
        print('Estado de sobrepeso')
    if imc >= 30:
        print('Estado de obesidad')


# Solicitamos la cantidad de personas a procesar
cantPersonas = int(input('Cuántas personas desea procesar: '))

# Definimos la condición mientras el contador sea menor al indicado
while contador < cantPersonas:
    pedirIMC()
    contador += 1
