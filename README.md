
# Transición Slider QStackedWidget

Este material fue extraido de [StackOverflow](https://stackoverflow.com/questions/52596386/slide-qstackedwidget-page "StackOverflow") y posteriormente adaptado.

**Indice**
  * [Recursos utilizados](#recursos-utilizados)
  * [Registros](#registros)
    -  [Controlador](#controlador)
    -  [Parámetros](#parámetros)
    -  [Condicionamiento y control](#condicionamiento-y-control)
    -  [Declarar indices](#declarar-indices)
    -  [Secuencia de transición](#secuencia-de-transición)
    -  [Configuraciones](#configuraciones)
    -  [Posicionamiento](#posicionamiento)
    -  [Animaciones](#animaciones)
    -  [Trayecto de animación](#trayecto-de-animación)
  * [Fuentes](#fuentes)
  * [Previsualización](#previsualización)

# Recursos utilizados

`pip install PySide2`

# Registros


### Controlador

indica si hay alguna transcicion ejecutandose.
```python
self.ctrl_animacion = False
```

### Parámetros
```python
self.raiz.btn1.clicked.connect(lambda : 
        self.transicion_stacked(index_final=0, indexSiguientes=[1,2]))
		
self.raiz.btn2.clicked.connect(lambda : 
        self.transicion_stacked(index_final=1, indexSiguientes=[2]))
		
self.raiz.btn3.clicked.connect(lambda : 
        self.transicion_stacked(index_final=2, indexSiguientes=[]))
```

```python
def transicion_stacked(self, index_final, indexSiguientes):
```

index_final: 
Index de pagina al que se dirije.

index_siguientes: 
Los index que siguen despues de el indicado del "0" le sigue [1,2], de "1" sigue [2]  pero del "2" no le sigue nadie [] (esto para tener un efecto avance y retroceso).

### Condicionamiento y control

**obtener index actual**

```python
index_inicio = self.raiz.miStack.currentIndex()
```

**condicionamiento**
1: no debe haber transciciones en ejecucion
2: el inicio y final no puede ser el mismo (index)

```python
if(self.ctrl_animacion)or(index_final==index_inicio):
    return
```

**Una vez ingresada el control se activara**

```python
self.ctrl_animacion = True
```

### Declarar indices

Declaramos el index `index_inicio` y `index_final` en la clase, esto por que se utlizara en los controles de transición.

```python
self.index_inicio = index_inicio
self.index_final = index_final
```


'''
### Secuencia de transición

**Direcionamiento de lienzo**
[↓] offsetx = 0; offsety = alto_stk
[↑] offsetx = 0; offsety = -alto_stk
[←] offsetx = ancho_stk; offsety = 0
[→] offsetx = -ancho_stk; offsety = 0

Para ello es sumamente importante obtener las dimenciones del widget

```python
ancho_stk = self.raiz.miStack.width()
alto_stk = self.raiz.miStack.height()
```

**Avance y retroceso**

Recapitulación de los parametros:

> index_siguientes: 
Los index que siguen despues de el indicado del "0" le sigue [1,2], de "1" sigue [2]  pero del "2" no le sigue nadie [] (esto para tener un efecto avance y retroceso).

```python
if(self.index_inicio in indexSiguientes):
    offsetx = -ancho_stk; offsety = 0
else:
    offsetx = ancho_stk; offsety = 0
```

### Configuraciones

Duración de efectos por milisegundos

```python
velocidad_tansicion = 600
```

En la transición podremos encontrar varios tipos en la documentacion de [QEasingCurve](https://doc.qt.io/qt-5/.html#Type-enum "QEasingCurve")

```python
efecto_transicion = QEasingCurve.OutCubic
```

### Posicionamiento

Posicionamiento del widget
```python
self.punto_actual = self.raiz.miStack.widget(self.index_inicio).pos()
self.punto_final = self.raiz.miStack.widget(self.index_final).pos()
```
mostrar el siguiente widged en la transición

```python
self.raiz.miStack.widget(self.index_final).show()
```

obtener punto de referencia

```python
offset = QPoint(offsetx, offsety)
```

### Animaciones

Crear un grupo de animacion para la transcicion de los widgets (esta se conectara con `self.realizarAnimacion`)

```python
animacion_stack = QParallelAnimationGroup(self.raiz.miStack, finished=self.realizarAnimacion)
```
Le agregamos la transcición de  entrada y salida

```python
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
```

Por último iniciamos la ejecución

```python
animacion_stack.start(QAbstractAnimation.DeleteWhenStopped)
```


### Trayecto de animación

Previamente se meciono al `self.realizarAnimacion` cuya funcionalidad sera el cambio de index y los movimientos de sus widgets.

Tambien una vez finalizado los efectos, el `self.ctrl_animacion` se restablecera, tomando el valor de `False`

```python
def realizarAnimacion(self):
    self.raiz.miStack.setCurrentIndex(self.index_final) # asignar index
    self.raiz.miStack.widget(self.index_inicio).hide()
    self.raiz.miStack.widget(self.index_inicio).move(self.punto_actual)

    # control de transicion (desactivado) /*/*/*/*/*/*/
    self.ctrl_animacion = False
```

# Fuentes

- [StackOverflow](https://stackoverflow.com/questions/52596386/slide-qstackedwidget-page "StackOverflow")

# Previsualización

![](https://1.bp.blogspot.com/-GHYa_LbYMGY/YFy63HczgBI/AAAAAAAAAJw/CBAEX-qohugFUMOOXBB7sqMlh1AtyMdQACLcBGAsYHQ/s1600/12461241.gif)