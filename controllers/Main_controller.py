

from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from views.MainView import Ui_MainWindow


class MainViewc(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# C

    #     # OPERACIN ESTUDIANTE
    # def cargar_Estudiantes_segun_grado_calificando(self, liEstuds):
    #     self.tblListEstud.setRowCount(0)
    #     self.tblListEstud.setRowCount(len(liEstuds))

    #     for (index_row, row) in enumerate(liEstuds):
    #         for (index_cell, cell) in enumerate(row):
    #             self.tblListEstud.setItem(
    #                 index_row, index_cell, QTableWidgetItem(str(cell)))

    # def limpiarTextosEstudiantes(self):
    #     self.txtRegNomEstud.setText("")
    #     self.txtRegNieEstud.setText("")
