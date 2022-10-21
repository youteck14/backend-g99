from cgi import print_arguments


class Person:
    height = 1.55
    weight = 80000
    sign = 'CAPRICORNIO'

    #metodos magicos: se reconocen por tener __ al inicio y al final __

    def __str__(self):
        #el metodo __str__ sirve para indicar que cuando se mande a llamar
        return "Welcome Person's Class"

    def greet(self):
        #self > en python en todas las funciones dentro de una clase (ahora las funciones pasan a 
        # llamarse METODOS) y para que pueda utilizar la propia configuracion de la clase (como sus
        # atributos y otros metodos) se declara con primer parametro la palabra 'self'
        texto = 'Hello I am a person and my height is '+str(self.height)
        print(texto)
    def saludar_cordialmente(self,nombre):
        texto = 'Hola {}, mucho gusto.'.format(nombre)
        return texto

eduardo = Person()#una copia 
gabriela = Person()
eduardo.height = 1.89
gabriela.height = 1.75

#retorna el nombre de la clase en formato string
print(Person.__name__)
print(eduardo)
print(eduardo.height)
print(gabriela.height)

eduardo.greet()
gabriela.greet()
result = eduardo.saludar_cordialmente('Angel')
print(result)
