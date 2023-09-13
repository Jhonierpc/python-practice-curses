# Calculadora de IMC
# IMC = Peso / (Altura * Altura)
# < 19: Delgado
# Entre 20 y 25: Normal
# Entre 26 y 30: Sobrepeso
# > 30: Obesidad

def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

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

pedirIMC()