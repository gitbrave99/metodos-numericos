from .Simpson import Simpson


class ConSimpson:
    def __init__(self) -> None:
        self._a = 0
        self._b = 0
        self._n = 0
        self._Sim = Simpson()
    
    def getH(self):
        return self._Sim.h
    
    def getI(self):
        return self._Sim.i

    def getXsubList(self):
        return self._Sim._xSub


    
    def getxFxList(self):
        return self._Sim._xFxlist

    def SimpsonUnTercioSimple(self,a,b,n,ecuacion):
        self._Sim._a=a
        self._Sim._b=b
        self._Sim._n=2
        self._Sim._ecuacion=ecuacion
        self._Sim.calcularH()
        self._Sim.calcularXsubList()
        self._Sim.evaluarFuncion()
        self._Sim.calcularXfxList()
        self._Sim.calcularISimpsonUnTercioSimple()

    def SimpsonUnTercioMultiple(self,a,b,n,ecuacion):
        self._Sim._a=a
        self._Sim._b=b
        self._Sim._n=n
        self._Sim._ecuacion=ecuacion
        self._Sim.calcularH()
        self._Sim.calcularXsubList()
        self._Sim.evaluarFuncion()
        self._Sim.calcularXfxList()
        self._Sim.calcularISimpsonUnTercioMultiple()
    
    def SimpsonTresOctavo(self,a,b,n,ecuacion):
        self._Sim._a=a
        self._Sim._b=b
        self._Sim._n=n
        self._Sim._ecuacion=ecuacion
        self._Sim.calcularH()
        self._Sim.calcularXsubList()
        self._Sim.evaluarFuncion()
        self._Sim.calcularXfxList()
        self._Sim.calcularISimpsonTresOctavosMultiple()

