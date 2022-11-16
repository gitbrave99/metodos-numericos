from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from views.MainView import Ui_MainWindow
from model.ConTrapecio import ConTrapecio
from model.ConSimpson import ConSimpson

class MainViewc(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._conT = ConTrapecio()
        self._conS = ConSimpson()
        self.cbxTipoRegla.currentIndexChanged.connect(self.evaluarMetodoCombo)
        self.btnCalcularMet.clicked.connect(self.evaluarMetodoButton)

    def evaluarMetodoCombo(self, indexCbx):
        self.listMetodos(indexCbx)
    
    def evaluarMetodoButton(self):
        opcion = int(self.cbxTipoRegla.currentIndex())
        if opcion > 0:
            self.listMetodos(opcion)

    def listMetodos(self,opcion):
        a = float(self.spinA.value())
        b = float(self.spinB.value())
        n = int(self.spinN.value())
        # ecuacion = '0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5'
        ecuacion = self.txtFormula.text()
        if ecuacion == "":
            return
        if opcion > 0:
            if opcion == 1:
                self.mostrarTrapecioSimple(a, b, ecuacion)
                self.mostrarOcultarDtNNc(2)
            if opcion == 2:
                self.mostrarTrapecioMultiple(a, b, n, ecuacion)
                self.mostrarOcultarDtNNc(1)
            if opcion == 3:
                self.mostrarSimpsonUnTercioSimple(a, b, 2, ecuacion)
                self.mostrarOcultarDtNNc(1)
            if opcion == 4:
                self.mostrarSimpsonUnTercioMultiple(a, b, n, ecuacion)
                self.mostrarOcultarDtNNc(1)
            if opcion == 5:
                self.mostrarSimpsonTresOctavos(a, b, 3, ecuacion)
                self.mostrarOcultarDtNNc(1)

    def mostrarTrapecioSimple(self, a, b, ecuacion):
        self._conT.trapecioSimple(a, b, ecuacion)
        self.txtI.setText(str(self._conT.getI()))
        self.txtFa.setText(str(self._conT.getFxa()))
        self.txtFb.setText(str(self._conT.getFxb()))

    def mostrarOcultarDtNNc(self, opcion):
        if opcion == 1:
            self.txtFa.setText("")
            self.txtFb.setText("")
        if opcion == 2:
            # self.txtH.setText("")
            # self.txtI.setText("")
            self.cargar_tb_xfx([])

    def mostrarTrapecioMultiple(self, a, b, n, ecuacion):
        self._conT.trapecioMultiple(a, b, n, ecuacion)
        self.txtH.setText(str(self._conT.getH()))
        self.txtI.setText(str(self._conT.getI()))

        # MOSTRAR X,FX EN LA TABLA
        # print(self._conT.getFxList())
        # print(len(self._conT.getFxList()))
        self.cargar_tb_xfx(self._conT.getxFxList())

    def mostrarSimpsonUnTercioSimple(self, a, b, n, ecuacion):
        self._conS.SimpsonUnTercioSimple(a, b, n, ecuacion)
        self.txtH.setText(str(self._conS.getH()))
        self.txtI.setText(str(self._conS.getI()))
        # MOSTRAR X,FX EN LA TABLA
        self.cargar_tb_xfx(self._conS.getxFxList())

    def mostrarSimpsonUnTercioMultiple(self, a, b, n, ecuacion):
        self._conS.SimpsonUnTercioMultiple(a, b, n, ecuacion)
        self.txtH.setText(str(self._conS.getH()))
        self.txtI.setText(str(self._conS.getI()))
        # MOSTRAR X,FX EN LA TABLA
        self.cargar_tb_xfx(self._conS.getxFxList())

    def mostrarSimpsonTresOctavos(self, a, b, n, ecuacion):
        self._conS.SimpsonTresOctavo(a, b, n, ecuacion)
        self.txtH.setText(str(self._conS.getH()))
        self.txtI.setText(str(self._conS.getI()))
        # MOSTRAR X,FX EN LA TABLA
        self.cargar_tb_xfx(self._conS.getxFxList())


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# C

    #     # OPERACIN ESTUDIANTE


    def cargar_tb_xfx(self, lisResp):
        self.tblXFx.setRowCount(0)
        self.tblXFx.setRowCount(len(lisResp))

        for (index_row, row) in enumerate(lisResp):
            for (index_cell, cell) in enumerate(row):
                self.tblXFx.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

    # def limpiarTextosEstudiantes(self):
    #     self.txtRegNomEstud.setText("")
    #     self.txtRegNieEstud.setText("")
