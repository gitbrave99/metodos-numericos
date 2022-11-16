from .Atributos import AtributoMetodos
from sympy import *

class Simpson(AtributoMetodos):
    def __init__(self) -> None:
        super().__init__()

    def calcularISimpsonUnTercioSimple(self):
        self._i = (self._h/3)*(self._fx[0] + 4*self._fx[1]+self._fx[-1])

    def calcularISimpsonUnTercioMultiple(self):
        self._i = (self._b-self._a)*((self._fx[0] + (4*self.getSumaIndicesImpares())+(2*self.getSumaIndicesPares())+self._fx[-1])/(3*self._n))
        print("suma impar: ",(4*self.getSumaIndicesImpares()))
        print("suma par: ",(2*self.getSumaIndicesPares()))
    
    
    def calcularISimpsonTresOctavosMultiple(self):
        self._i = (self._b-self._a)*((self._fx[0] + (3*self._fx[1])+(3*self._fx[2])+self._fx[-1])/8)

        print(f'x0 ={self._fx[0]} x1= {self._fx[1]} x2= {self._fx[2]} x3= {self._fx[-1]}')
    
    def getSumaIndicesImpares(self):
        sumImpar=0
        for i in range(1,self._n):
            if i % 2 !=0:
                sumImpar+=self._fx[i]
        return sumImpar

    def getSumaIndicesPares(self):
        sumPar=0
        for i in range(1,self._n-1):
            if i % 2 ==0:
                sumPar+=self._fx[i]
        return sumPar

    def calcularH(self):
        self._h = ((self._b-self._a) / self._n)
        print(f'h: {self._h} a= {self._a} b= {self._b} n= {self._n}')

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
        print(self._xSub)


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

