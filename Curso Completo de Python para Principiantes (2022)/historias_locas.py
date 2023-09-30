# concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ____________.

# organizacion = 'jhonier'

# print('Aprende a programar con '  + organizacion)
# print('Aprende a programar con {}'.format(organizacion))
# print(f'Aprende a programar con {organizacion}')

adj = input('Adjectivo: ')
vervo1 = input('Vervo: ')
vervo2 = input('Vervo: ')
objetivos = input('objetivo: ')


madlib = f'Programar es tan {adj}! Siempre me emociona porque me encanta {vervo1} problemas. Aprende a {vervo2} con Jhonier y alcanza tus {objetivos}'

print(madlib)