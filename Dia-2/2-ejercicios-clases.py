# Crear una clase llamada Persona en la cual se guarden: nombre, fecha_nacimiento, 
# nacionalidad y dni. Crear otra clase llamada Alumno que va a heredar la clase Persona 
# y ademas va a tener sus atributos: num_seguro, num_emergencia, matriculado (Boolean), 
# el alumno tendra un metodo llamado mostrar_datos y ademas otro metodo llamado matricular 
# en el cual si esta matriculado no se podra matricular, caso contrario, si. Y tambien tener 
# otra clase Profesor que va a tener cta_pago y maestria (str) y el profesor puede mostrar 
# su cta_pago y ademas si tiene maestria al momento de mostrar la cta_pago indicar que se le 
# tiene que agregar 100 soles.

class Persona:
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.dni = dni

class Alumno(Persona):
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni,num_seguro,num_emergencia,matriculado):
        self.num_seguro = num_seguro
        self.num_emergencia = num_emergencia
        self.matriculado = matriculado
        super().__init__(nombre,fecha_nacimiento,nacionalidad,dni)

    def mostrar_datos(self):
        return {
            'nombre': self.nombre,
            'fecha de nacimiento': self.fecha_nacimiento,
            'nacionalidad': self.nacionalidad,
            'dni': self.dni,
            'numero de seguro': self.num_seguro,
            'numero de emergencia': self.num_emergencia,
            'matriculado': self.matriculado
        }

    def matricular(self):
        if self.matriculado == True:
            print("Ya estas matriculado")
        else:
            print("Se matriculo correctamente")

class Profesor:
    def __init__(self,cuenta_pago, maestria):
        self.cuenta_pago = cuenta_pago
        self.maestria = maestria

    def mostrarDatos(self):
        
        if self.maestria.lower() == 'si':
            print('Numero de cuenta: ',self.cuenta_pago , 'ademas se le tiene que agregar 100 soles')
        else:
            print('Numero de cuenta: ',self.cuenta_pago)


persona = Persona('Yohan', '14 de Junio', 'peruano', 71066274)
alumno = Alumno('Yohan', '14 de Junio', 'peruano', 71066274, 21937128, 205132, False)
print(alumno.mostrar_datos())
alumno.matricular()
profesor = Profesor(12309218, 'NO')
profesor.mostrarDatos()