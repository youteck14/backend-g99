

#herencia

class Usuario:
    def __init__(self,nombre,apellido,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_resumen(self):
        return {
            'nombre':self.nombre,
            'apellido': self.apellido,
            'correo': self.correo
        }

class Alumno(Usuario):
    def __init__(self,nombre,apellido,correo,telefono_emergencia):
        self.telefono_emergencia = telefono_emergencia
        super().__init__(nombre,apellido,correo)


    def saludar(self):        
        print('hola yo soy {} la clase alumno'.format(self.nombre))

    

    def mostrar_resumen(self):

        resumen = super().mostrar_resumen()
        resumen['telefono_emergencia'] = self.telefono_emergencia
        return resumen
       

usuario01 = Usuario(nombre = 'Yohan', apellido='Romero', correo='yohanrr86@gmail.com')
usuario02 = Usuario('Alejandra', 'Perez', 'aperez@gmail.com')
usuario03 = Usuario(correo='sanson121416@gmail.com', apellido='Dias', nombre='Javier')

print(usuario01.mostrar_resumen())

alumno01 = Alumno('Juan','Martinez', 'jmartinez@yahoo.es', '970747424')
alumno01.saludar()
print(alumno01.mostrar_resumen())