from turtle import position


def sumar(num1,num2):
    return num1+num2



def sumar_n_numero(*args):
    # * PARAMETROS ILIMITADOS 
    suma =0
    for n in args:
        suma = n + suma
    print(suma)

    suma2 =0
    """ for posicion in range(0,len(args)):
        print(posicion)
        suma2 = suma2 + args[position]
    print(suma2) """

""" print(sumar(5,10)) """
sumar_n_numero(10,5,18,7,22,56,89)

def filtro(**kwargs):
    #kwards > keyword argument > recibiremos un numero ilimitado de 
    #parametros pero utilizando el nombre del parametro y su valor
    # **PARAMETROS ILIMITADOS
    for key in kwargs.keys():#key me devulve un arreglo con todas las llaves
        valor=kwargs.get(key)
        print(key,':',valor)

    """ for key,valor in enumerate(kwargs):
        
        print(key,valor) """
   

filtro(nombre = 'eduardo', edad=30, sexo='M')

filtro(nombre = 'eduardo', edad=30, sexo='M',nacionalidad='PERUANO')

curso= {
    'nombre': 'Matematica',
    'dificultad': 'Intermedio',
    'experiencia': 'Ninguna',
    0:'hola'
}

print(curso)
print(curso.keys())
print(curso.values())
print(curso[0])
print(curso['dificultad'])
print(curso.get('calificacion'))
print(curso.get('nombre','No hay'))
#modificar valores en el diccionario, si esa llave no existe, entonces se creara
curso['mas_info'] = 'esta es una informacion adicional'
print(curso)
#metodo .get SOLAMENTE sirve para visualizar la información