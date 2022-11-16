class AtributoMetodos:
    def __init__(self) -> None:
        self._a = 0
        self._b = 0
        self._fa = 0
        self._fb = 0
        self._n = 0
        self._h = 0
        self._i = 0
        self._xSub = []
        self._fx = []
        self._ecuacion = ""
        self._xFxlist=[]
    
    @property
    def xFxlist(self):
        return self._xFxlist
        
    @xFxlist.setter
    def xFxlist(self,list):
        self._xFxlist= list

    @property
    def ecuacion(self):
        return self._ecuacion

    @ecuacion.setter
    def ecuacion(self, ecuacion):
        self._ecuacion = ecuacion
    
    @property
    def xSub(self):
        return self._xSub

    @xSub.setter
    def xSub(self, xSub):
        self._xSub = xSub

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def fa(self):
        return self._fa

    @fa.setter
    def fa(self, fa):
        self._fa = fa

    @property
    def fb(self):
        return self._fb

    @fb.setter
    def fb(self, fb):
        self._fb = fb

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        self._n = n

    @property
    def h(self):
        return round(self._h, 4)

    @h.setter
    def h(self, h):
        self._h = h

    @property
    def i(self):
        return round(self._i, 4)

    @i.setter
    def i(self, i):
        self._i = i

    def calcularH(self, a, b, n):
        return (b-a)/n
