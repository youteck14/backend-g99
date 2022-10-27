#replicar la funcionabilidad de la libreria CamelCase

#HINT : los string en python son considerados listas
#texto = 'eduardo' > text[0] = 'e'.....

entrada = input("Ingrese una cadena de texto: ")

texto = 'Hola como estan'

class CamelCasePropia:
    def __init__(self):
        pass

    def hump(self,texto):
        nuevoTexto = texto.split(' ')
        palabrasMayus = []

        for palabra in nuevoTexto:
            palabrasMayus.append(palabra.capitalize())
        print(palabrasMayus)
        nuevoTextoMayus = ' '.join(palabrasMayus)
        return nuevoTextoMayus

cc = CamelCasePropia()
print(cc.hump(texto))
