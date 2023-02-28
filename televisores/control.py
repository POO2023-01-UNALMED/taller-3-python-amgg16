class Control:
   
   def __init__(self):
       self._tv=None

   def turnOff(self):
       self._tv.turnOff()
    
   def turnOn(self):
       self._tv.turnOn()
    
   def canalDown(self):
       self._tv.canalDown()
       
   def canalUp(self):
       self._tv.canalUp()

   def volumenUp(self):
       self._tv.volumenUp()

   def volumenDown(self):
       self._tv.volumenDown()

   def setCanal(self,canal):
       self._tv.setCanal(canal)
       
   def enlazar(self,tv):
       self._tv=tv
       tv.setControl(self)
    
   def getTv(self):
       return self._tv
   
   def setTv(self,tv):
       self.tv=tv