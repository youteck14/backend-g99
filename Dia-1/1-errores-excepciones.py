from multiprocessing.sharedctypes import Value


try:
    #print(10/0)

    int('a')
except ZeroDivisionError:
    #aca ingresara si el error es de tipo ZeroDivisionError
    print('Hubo un error al dividir entre cero')
except ValueError:
    #aca entrara si hubo un error de conversion a entero
    print('Error al convertir el numero')
except Exception as error:
    #.args es el atricuto de toda instancia de Excepcion que se devolvera el porque se dio ese
    #error(argumentos)
    print(error.args) #argas son los argumentos de la descripcion del error
    print("Hubo un error al dividir entre cero")

print('Yo no soy un error')


try:
    #args son los argumentos que nosotros indicaremos o que recibiremos cuando se de un error, en este
    #atributo se podran obtener todos los argumentos del porque se dio ese error.
    raise Exception('eres menor de edad', 'no eres peruano' , 'no eres femenino')#throw new Error()
    #raise emitimos un error<
except Exception as error:
    print(error.args)


try:
    resultado = 5/1
    raise Exception('Error desconocido')
except Exception as error:
    print(error.args)

else:
    #en el caso que el codigo ejecutase sin ningun error (sin ingresar al except)
    print('La operacion se realizo exitosamente')
finally:
    #ingresa si la ejecucion estuvo bien o si ingresa al except
    print('Si la operacion estuvo bien o mal igual se ejecuta')


#Recibir po r el teclado un numero

#luego tratar de convertir ese numero  a un entero (si no se puede indicar que el valor es
# incorrecto). Sumar 10 mas ese numero ingresado a imprimir el resultado.

numero = input("Ingresa un numero: ")

try:
    numero = int(numero)
    suma = 10 + numero
    print("La suma es la siguiente: ",suma)
except ValueError:
    print("El valor ingresado es un string y deberia de ser un numero")
except Exception as error:
    print(error.args)
finally:
    print("convirtiendo y sumando un numero")