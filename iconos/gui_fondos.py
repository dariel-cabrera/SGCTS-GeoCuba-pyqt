import sys
from imagenes import *
# pyrcc5 imagenes.py -o imagenes.qrc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from messagebox import msg_error, msg_about
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import cv2
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import mediapipe as mp
import numpy as np


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login_modern.ui", self)
        self.frame.mouseMoveEvent = self.moveWindow
        self.ingresar.clicked.connect(self.gui_login)
        self.salir.clicked.connect(self.exit)
        timer = QTimer(self)
        timer.timeout.connect(self.mostrar_reloj)
        timer.start(1000)

    def exit(self):
        app.exit()
        sys.exit()

    def mostrar_reloj(self):
        tiempo = QTime.currentTime()
        display2text = tiempo.toString("hh:mm:ss")
        self.reloj.setText(display2text)

    def gui_login(self):
        name = self.name.text()
        password = self.password.text()
        if len(name) == 0 or len(password) == 0:
            msg_error("Error","No hay datos")
        elif name == "Yered" and password == "123456":
            self.window_access()
        else:
            msg_error("Error", "Los datos no coinciden")

    def window_access(self):
        ventana_2 = Gui_access()
        widget.addWidget(ventana_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(768)
        widget.setFixedWidth(1366)

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.gui_login()

class Gui_access(QMainWindow):
    filename = None
    final_image = None

    def __init__(self):
        super(Gui_access, self).__init__()
        loadUi("gui_fondos.ui", self)
        self.cerrar.clicked.connect(self.regresar_login)
        self.frame.mouseMoveEvent = self.moveWindow
        self.soporte.clicked.connect(self.soporte_gui)
        self.tip.clicked.connect(self.tip_gui)
        self.borrar.clicked.connect(self.limpiar)
        self.abrir.clicked.connect(self.cargarImagen)
        self.guardar.clicked.connect(self.dialog)
        self.imagen.clicked.connect(self.cargarImagen_2)
        self.salir.clicked.connect(self.exit)
        self.min.clicked.connect(self.minimizar)

    def cargarImagen(self):
        global filename
        filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        imagen = cv2.imread(filename)
        self.setPhoto(imagen)

    def setPhoto(self,image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imagen = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        imagen = imagen.scaled(350, 350, Qt.KeepAspectRatio)
        self.img_original.setPixmap(QtGui.QPixmap.fromImage(imagen))
        self.label_img_ori.setText("Imagen original")

    def setPhoto_2(self,image):
        global final_image
        final_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        imagen = QImage(final_image, final_image.shape[1], final_image.shape[0], final_image.strides[0],
                        QImage.Format_RGBA8888)
        imagen = imagen.scaled(350, 350, Qt.KeepAspectRatio)
        self.img_tran.setPixmap(QtGui.QPixmap.fromImage(imagen))
        self.label__img_tran.setText("Imagen sin fondo")
        self.next.setStyleSheet("border-image: url(:/iconos-imagenes/next.png);")

    def cargarImagen_2(self):
        global filename, final_image
        self.uniendo(filename)
        final_image = cv2.imread("mientras.png")
        self.setPhoto_2(final_image)

    def uniendo(self, imagen):
        # Iniciamos la función de selfie segmentation de mediapipe
        mp_selfie_segmentation = mp.solutions.selfie_segmentation

        # Leemos la imagen
        img = cv2.imread(imagen)
        # Redimensionamos la imagen
        alto, ancho, _ = img.shape
        img = cv2.resize(img, (int((ancho/1)),int((alto/1))))
        print(img.shape)

        self.pre = "foto.png"


        with mp_selfie_segmentation.SelfieSegmentation(model_selection = 0) as selfie_segmentation:
            # Convertimos la imagen de BGR a RGB antes del procesamiento
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Teniendo la imagen en RGB podemos aplicarle el método de selfie segmentation, lo que hace es
            # buscar el contorno de la persona.
            result = selfie_segmentation.process(img_rgb)

            # Binarizamos el resultado anterior para que solo haya 0 y 1 (o sea en blanco y negro).
            _, thresh = cv2.threshold(result.segmentation_mask, 0.75, 255, cv2.THRESH_BINARY)
            # Imprimimos
            #print(thresh.dtype)
            # Cambiamos de float32 a uint8
            thresh = thresh.astype(np.uint8)
            # Suavizamos la imagen
            #thresh = cv2.medianBlur(thresh, 13)

            # Invertimos el negro a blanco y el blanco a negro
            thresh_not = cv2.bitwise_not(thresh)

            # -- Proceso para encontrar el contorno de la persona -- #
            img_contours = cv2.findContours(thresh_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            img_contours = sorted(img_contours, key=cv2.contourArea)

            for i in img_contours:
                if cv2.contourArea(i) > 100:
                    break
            # -- Fin de proceso para encontrar el contorno de la persona -- #


            bg = cv2.imread("canal_alpha.png")
            bg = cv2.resize(bg, (int(ancho/1),int(alto/1)))

            fondo = cv2.bitwise_and(bg, bg, mask=thresh_not)

            fg = cv2.bitwise_and(img, img, mask=thresh)

            salida = cv2.add(fondo, fg)

            cv2.imwrite(self.pre, salida)
            self.proce("mientras.png")


    def proce(self, nombre):
        img = Image.open(self.pre)
        img = img.convert("RGBA")

        imgnp = np.array(img)

        white = np.sum(imgnp[:, :, :3], axis=2)
        white_mask = np.where(white == 255 * 3, 1, 0)

        alpha = np.where(white_mask, 0, imgnp[:, :, -1])

        imgnp[:, :, -1] = alpha

        img_2 = Image.fromarray(np.uint8(imgnp))
        img_2.save(nombre, "PNG")


    def dialog(self):
        global final_image
        file, check = QFileDialog.getSaveFileName(None, "Guardar archivo",
                                                  "", "image (*.png)")
        if check:
            self.proce(file)
            msg_about("Guardado", "La imagen se ha guardado correctamente")

    def limpiar(self):
        self.img_original.clear()
        self.img_tran.clear()
        self.label__img_tran.clear()
        self.label_img_ori.clear()
        self.next.setStyleSheet("")

    def tip_gui(self):
        msg_about("Tip", "Suscríbete a Terrones Digital ;)")

    def soporte_gui(self):
        msg_about("Soporte", "Si tiene problemas con el software \n puede"
                             " escribir al correo digitalterrones@gmail.com")

    def regresar_login(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedHeight(768)
        widget.setFixedWidth(1366)

    def minimizar(self):
        widget.showMinimized()

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def exit(self):
        app.exit()
        sys.exit()


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(768)
widget.setFixedWidth(1366)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")