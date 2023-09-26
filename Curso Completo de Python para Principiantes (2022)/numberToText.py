def crear_diccionario(numero, diccionario):
    if str(numero) not in diccionario:
        diccionario[str(numero)] = num_to_text(numero)
    return diccionario


def num_to_text(numero):
    numeros_texto = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    return numeros_texto[numero]


# Diccionario inicial vacío
numeros = {}

while True:
    try:
        numero = int(
            input("Digite el numero que desea transformar a texto (o ingrese cualquier otro valor para salir): ")
            )
        texto = num_to_text(numero)
        numeros = crear_diccionario(numero, numeros)

        print(f'El numero {numero} en texto es: {texto}')
        print('Diccionario actualizado:')
        for clave, valor in numeros.items():
            print(f'{clave}: {valor}')
    except ValueError:
        break
