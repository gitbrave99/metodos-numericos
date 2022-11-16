from .Trapecio import Trapecio


class ConTrapecio:
    def __init__(self) -> None:
        self._Trap = Trapecio()

    def trapecioSimple(self, a, b,ecuacion):
        self._Trap.a = a
        self._Trap.b = b
        self._Trap.ecuacion = ecuacion
        self._Trap.fa = self._Trap.getFxVal(a)
        self._Trap.fb = self._Trap.getFxVal(b)
        print(f'fb= {self._Trap.fb} fb = {self._Trap.fa}')
        self._Trap.calcularITrapecioSimple()
 
    def getI(self):
        return self._Trap.i

    def getFxa(self):
        return self._Trap.fa

    def getFxb(self):
        return self._Trap.fb

    def getH(self):
        return self._Trap.h

    def getXsubList(self):
        return self._Trap._xSub
    
    def getFxList(self):
        return self._Trap._fx
    
    def getxFxList(self):
        return self._Trap._xFxlist

    def trapecioMultiple(self, a, b, n,ecuacion):
        self._Trap.a = a
        self._Trap.b = b
        self._Trap.n = n
        self._Trap.ecuacion=ecuacion
        # self._Trap.fa = 0.2
        # self._Trap.fb = 0.232
        self._Trap.calcularH()
        self._Trap.calcularXsubList()
        self._Trap.evaluarFuncion()
        self._Trap.calcularXfxList()
        self._Trap.calcularItrapecioMultiple()
        self._Trap._xSub.append(self._Trap._fx)
        