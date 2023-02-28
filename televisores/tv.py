class TV:

    _numTV=0

    def __init__(self,marca,estado,canal=1,precio=500,volumen=1,control=None):
        self._marca=marca
        self._canal=canal
        self._precio=precio
        self._estado=estado
        self._volumen=volumen
        self._control=control
        TV._numTV+=1
    
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca=marca

    def getControl(self):
        return self._Control
    
    def setControl(self, Control):
        self._Control=Control

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio=precio

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if ((self._estado==True) and (volumen>=0 and volumen <=7)):  
            self._volumen=volumen

    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        if ((self._estado==True) and (canal>=1 and  canal<=120)):  
            self._canal=canal

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls,numTV):
        cls._numTV=numTV

    def turnOff(self):
        self._estado=False
    
    def turnOn(self):
        self._estado=True

    def getEstado(self):
        return self._estado
    
    def canalUp(self,canal):
        if self._estado==True and canal>1 and canal<120:
            self._canal+=1
    
    def canalDown(self,canal):
        if self._estado==True and canal>1 and canal<120:
            self._canal-=1

    def volumenUp(self,volumen):
        if self._estado==True and volumen>0 and volumen<7:
            self._volumen+=1

    def volumenDown(self,volumen):
        if self._estado==True and volumen>0 and volumen<7:
            self._volumen-=1

