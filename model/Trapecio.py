from .Atributos import AtributoMetodos
from sympy import *


class Trapecio(AtributoMetodos):
    def __init__(self) -> None:
        super().__init__()

    def calcularITrapecioSimple(self):
        self._i = (self._b-self._a)*(((self._fa+self._fb)) / 2)
    
    def calcularFA(self):
        pass

    def calcularFB(self):
        pass

    def calcularItrapecioMultiple(self):
        self._i = (self._b-self._a) * (((self._fx[0]+(2*self.sumaRangoFx()) + self._fx[-1]))/(2 * self._n))
        print(self.sumaRangoFx())
        

    def calcularXsubList(self):
        self._xSub = []
        hacum = 0
        # self._xSub[0]=self._a
        for i in range(self._n+1):
            if i == 0:
                # hacum+=(self._a+self._h)
                self._xSub.append((f'X0', round(self._a, 4)))
                continue
            hacum += self._h
            self._xSub.append((f'X{i}', round(hacum, 4)))
# -------------------------------------

    def calcularXfxList(self):
        self._xFxlist = []
        hacum = 0
        # self._xSub[0]=self._a
        for i in range(self._n+1):
            if i == 0:
                # hacum+=(self._a+self._h)
                self._xFxlist.append((f'X0', round(self._a, 4), f'fx(0)', self.getFxVal(self._a)))
                continue
            hacum += self._h
            self._xFxlist.append((f'X{i}', round(hacum, 4), f'fx({i})', self.getFxVal(hacum)))
        # print(self._xFxlist)

    def getFxVal(self, val):
        x = Symbol('x')
        rfx = round(simplify(self._ecuacion).subs(x, val), 4)
        return rfx

# -------------------------------------
    def evaluarFuncion(self):
        x = Symbol('x')
        self._fx=[]
        for i in range(self._n+1):
            xi = float(self._xSub[i][1])
            rfx = round(simplify(self._ecuacion).subs(x, xi), 4)
            self._fx.append( rfx)
        # LLENAR PARA MOSTRAR TODO EN LA TABLA
        # print(f'efe = {self._fx}')
        # print(self._fx)
        
    def calcularH(self):
        self._h = ((self._b-self._a) / self._n)

    def sumaRangoFx(self):
        return sum(self._fx[1:-1])
        
        
