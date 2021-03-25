# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow,QApplication
from PySide2.QtCore import (QPoint,QEasingCurve, QParallelAnimationGroup, 
                            QPropertyAnimation, QAbstractAnimation)

# importar diseño
from view.ui_Principal import Ui_Principal

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        self.raiz = Ui_Principal()
        self.raiz.setupUi(self)

        # conexion de botones /*/*/*/*/*/*/
        self.raiz.btn1.clicked.connect(lambda : 
                self.transicion_stacked(index_final=0, indexSiguientes=[1,2]))
        self.raiz.btn2.clicked.connect(lambda : 
                self.transicion_stacked(index_final=1, indexSiguientes=[2]))
        self.raiz.btn3.clicked.connect(lambda : 
                self.transicion_stacked(index_final=2, indexSiguientes=[]))

        # control de transicion /*/*/*/*/*/*/
        'indica si hay alguna transcicion ejecutandose'
        self.ctrl_animacion = False

    def transicion_stacked(self, index_final, indexSiguientes):#, direction='vertical'):
        """ Animacion de cambio del StackedWidget """

        '''
        # PARAMETROS
        *index_final: 
            Index de pagina al que se dirije.

        *index_siguientes: 
            Los index que siguen despues de el indicado
            del "0" le sigue [1,2], de "1" sigue [2] 
            pero del "2" no le sigue nadie []
            (esto para tener un efecto avance y retroceso)
        '''

        # obtener index actual /*/*/*/*/*/*/
        index_inicio = self.raiz.miStack.currentIndex()

        # condicionamiento /*/*/*/*/*/*/
        '1: no debe haber transciciones en ejecucion'
        '2: el inicio y final no puede ser el mismo (index)'
        if(self.ctrl_animacion)or(index_final==index_inicio):
            return

        # control de transicion (activo) /*/*/*/*/*/*/
        self.ctrl_animacion = True

        # index /*/*/*/*/*/*/
        self.index_inicio = index_inicio
        self.index_final = index_final

        '''
        #-TANSICIONES-*-*-*-*-*-*-*-*-*-*-*

        ↓ offsetx = 0; offsety = alto_stk
        ↑ offsetx = 0; offsety = -alto_stk
        ← offsetx = ancho_stk; offsety = 0
        → offsetx = -ancho_stk; offsety = 0

        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '''

        # tamaño de widget para transciciones /*/*/*/*/*/*/
        ancho_stk = self.raiz.miStack.width()
        alto_stk = self.raiz.miStack.height()

        # efecto de avance y retroceso /*/*/*/*/*/*/
        if(self.index_inicio in indexSiguientes):
            offsetx = -ancho_stk; offsety = 0
        else:
            offsetx = ancho_stk; offsety = 0

        # configuraciones /*/*/*/*/*/*/
        velocidad_tansicion = 600
        efecto_transicion = QEasingCurve.OutCubic # OutCubic | InOutQuint | OutExpo

        # posicionamiento del widget /*/*/*/*/*/*/
        self.punto_actual = self.raiz.miStack.widget(self.index_inicio).pos()
        self.punto_final = self.raiz.miStack.widget(self.index_final).pos()

        # mostrar el siguiente widged en la transicion /*/*/*/*/*/*/
        self.raiz.miStack.widget(self.index_final).show()

        # obtener punto de referencia /*/*/*/*/*/*/
        offset = QPoint(offsetx, offsety)

        # animacion de transcicion de widgets /*/*/*/*/*/*/
        animacion_stack = QParallelAnimationGroup(self.raiz.miStack, finished=self.realizarAnimacion)

        animacion_inicio = QPropertyAnimation(
            self.raiz.miStack.widget(self.index_inicio),b"pos",
            duration=velocidad_tansicion, easingCurve=efecto_transicion,
            startValue=self.punto_actual,
            endValue=self.punto_final - offset)

        animacion_final = QPropertyAnimation(
            self.raiz.miStack.widget(self.index_final),b"pos",
            duration=velocidad_tansicion, easingCurve=efecto_transicion,
            startValue=self.punto_actual + offset,
            endValue=self.punto_final)

        animacion_stack.addAnimation(animacion_inicio)
        animacion_stack.addAnimation(animacion_final)

        # iniciar efecto /*/*/*/*/*/*/
        animacion_stack.start(QAbstractAnimation.DeleteWhenStopped)

    def realizarAnimacion(self):
        self.raiz.miStack.setCurrentIndex(self.index_final) # asignar index
        self.raiz.miStack.widget(self.index_inicio).hide()
        self.raiz.miStack.widget(self.index_inicio).move(self.punto_actual)

        # control de transicion (desactivado) /*/*/*/*/*/*/
        self.ctrl_animacion = False


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
