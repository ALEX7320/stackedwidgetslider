# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow,QApplication

# importar diseño
from view.ui_Principal import Ui_Principal

# transicion para el stacked
from Funcion_EfectoSlider import Clase_EfectoSlider

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        self.raiz = Ui_Principal()
        self.raiz.setupUi(self)

        # indicamos el stack a utilizar /*/*/*/*/*/*/
        self.raizefestack = Clase_EfectoSlider(self.raiz.stackedWidget)

        # conexion de botones /*/*/*/*/*/*/
        self.raiz.btn1.clicked.connect(lambda : 
            self.raizefestack.transicion_stacked(index_final=0, indexSiguientes=[1,2]))

        self.raiz.btn2.clicked.connect(lambda : 
            self.raizefestack.transicion_stacked(index_final=1, indexSiguientes=[2]))

        self.raiz.btn3.clicked.connect(lambda : 
            self.raizefestack.transicion_stacked(index_final=2, indexSiguientes=[]))


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
