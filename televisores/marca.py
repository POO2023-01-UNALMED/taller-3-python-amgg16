class Marca:

    def __init__(self,nombre):
        self._nombre=nombre

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self._nombre=nombre