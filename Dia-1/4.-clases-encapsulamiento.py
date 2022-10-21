class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        #__atributo > estaremos indicando que sera privado y por ende no puede ser accedido
        #desde fuera de la clase PRIVADO
        self.__ventas =[]
        #_atributo > atributo PROTEGIDO en Python mas que todo funciona para cuando queremos
        #utilizarlo con herencia
        self._precio_mayorista = 100

    def generar_venta(self,fecha,cliente,cantidad):
        venta = {
            'fecha':fecha,
            'cliente': cliente,
            'cantidad': cantidad
        }
        self.__ventas.append(venta)
        print(self.__sacar_igv(self.precio))
        print('Venta registrada exitosamente')

    def mostrar_ventas(self):
        return self.__ventas

    def __sacar_igv(self,precio):
        return precio - (precio * 0.18)

detergente = Producto(nombre = "Detergente Sapito", precio = 4.50, cantidad = 50)
detergente.nombre = 'Detergente Lechuga'
print(detergente.nombre)

detergente.generar_venta(fecha='2022-10-19', cliente='Eduardo de Rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='Julissa Perez', cantidad=30)
detergente.generar_venta(fecha='2022-10-30', cliente='Franco Portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='Michelle Ordoñez', cantidad=15)

print(detergente.mostrar_ventas())

""" print(detergente.__sacar_igv(80.00)) """

