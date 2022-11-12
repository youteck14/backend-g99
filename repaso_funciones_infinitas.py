def prueba(**argumentos):
    print(argumentos)

prueba(nombre='edwuardo', apellido='de rivero')

persona = {
    'nombre': 'eduwardo',
    'apellido': 'de rivero'
}

prueba(persona = persona)
#cuando nosotros en una funcion pasamos un Diccionario pero con dobre asterisco antes (**) significa que scara las llaves(keys) y la colocara como parametro de la funcion y sus valores como los valores de esos parametros
prueba(**prueba)
prueba(nombre = persona['nombre'], apellido= persona['apellido'])

#si usamos una funcion con paramteros definidos entonces tenemos que indicar en el diccionario ESEMISMO NOMBRE DE PARAMETROS ya qye si es diferente, arrojara un error
def saludar(nombre):
    print(nombre)

usuario = {
    'nombre':'eduardo'
}
usuario2 = {
    'nombrecito': 'juanito'
}
saludar(**usuario)
# Esto me arrojara un error ya que el parametro 'nombrecito no concuerda 