name = input('Digita tu nombre: ')
edad = input('Cuantos años tienes?: ')

def operation(oper):
    num1 = int(input('Digita el primer numero: '))
    num2 = int(input('Digita el segundo numero: '))

    def suma(n1, n2):
        resultado = n1 + n2
        print('El resultado de la suma es: ' + str(resultado))

    def resta(n1, n2):
        resultado = n1 - n2
        print('El resultado de la resta es: ' + str(resultado))

    def multiplicacion(n1, n2):
        resultado = n1 * n2
        print('El resultado de la multiplicacion es: ' + str(resultado))

    if operacion == 'Suma':
        suma(num1, num2)

    if operacion == 'Resta':
        resta(num1, num2)

    if operacion == 'Multiplicacion':
        multiplicacion(num1, num2)

print('Hola ' + name + 'Tu tienes ' + edad + ' años.')
operacion = input('Que operacion deseas hacer?: ')
operation(operacion)

