from deep_translator import GoogleTranslator

text = input('Qué desea traducir: ')

traductor = GoogleTranslator(source = 'es', target = 'en')
resultado = traductor.translate(text)
print(resultado + 'Este es el resultado')
