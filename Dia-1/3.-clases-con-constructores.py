class Documento:
    def __init__(self, tipo, num_paginas, editable,contenido):
        #en el constructor definimos un nuevo atributo este se creara para toda la clase
        self.tipo = tipo
        self.num_paginas = num_paginas
        self.editable = editable
        self.contenido = contenido

    def editar_documento(self,nuevo_contenido):

        if(self.editable == False):
            print("El archivo no se puede modificar")
        else:
            self.contedido = nuevo_contenido
            print("El archivo fue modificado")

"""     def editar_documento(self,nuevo_contenido):
        self.nuevo_contenido = nuevo_contenido

        if(self.editable):
            self.contenido = self.nuevo_contenido
            print(self.nuevo_contenido)
        else:
            print('No se puede editar')

mi_curriculum = Documento(tipo = 'PDF', num_paginas=80, editable=False, contenido='Soy developer')
proforma_pagina_web = Documento(tipo='Word', num_paginas=3, editable=True, contenido='La pagina web vale 2500 soles')

mi_curriculum.editar_documento='Ahora soy qa'
proforma_pagina_web.editar_documento='La pagina web vale 4000 soles' """

    


mi_curriculum = Documento(tipo = 'PDF', num_paginas=80, editable=False, contenido='Soy developer')

proforma_pagina_web = Documento(tipo='Word', num_paginas=3, editable=True, contenido='La pagina web vale 2500 soles')

mi_curriculum.editar_documento(nuevo_contenido='Ahora soy qa')

proforma_pagina_web.editar_documento(nuevo_contenido='La pagina web vale 4000 soles')