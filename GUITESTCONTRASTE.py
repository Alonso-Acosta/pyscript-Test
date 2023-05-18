import ctypes
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QGuiApplication, QImage, QPixmap
import numpy as np
from GUITest2 import *
import sys
from skimage import exposure
from skimage import io, draw
from scipy import fftpack



class GuiContraste(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__();
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);
        self.showFullScreen()
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.ancho, self.alto =user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.dato = np.loadtxt("datos3.txt",dtype=object)
        self.auxEstimulo = self.dato[-1,0]
        self.maxEstimulos = self.dato.shape[0]
        self.EstimuloActual = 0
        self.timer = QTimer()
        self.ResultadosPrueba = []
        self.i = 0
        self.contrasteActual = 0
        self.FiltroActual = 0
        self.tamañoActual = 0
        self.auxEstimuloIndi = 0
        self.auxResulIndi = 1
        self.MatrizCorrecta = []
        self.matriz_letras = []
        self.MatrizR = []
        self.cargarImagenes(self.i,1)

    def cargarImagenes(self,i,auxResul):
        tex = self.dato[i, 6]
        letras = np.array(list(tex))
        self.MatrizCorrecta = letras
        if self.auxEstimulo == "2":
            self.ui.Foto1.setVisible(False)
            if len(letras) == 5:
                #Cargar letras:
                self.letra1 = 'Sloan2/Sloan_{}.png'.format(letras[0])
                self.letra2 = 'Sloan2/Sloan_{}.png'.format(letras[1])
                self.letra3 = 'Sloan2/Sloan_{}.png'.format(letras[2])
                self.letra4 = 'Sloan2/Sloan_{}.png'.format(letras[3])
                self.letra5 = 'Sloan2/Sloan_{}.png'.format(letras[4])
                if auxResul == 1:
                    self.contrasteActual = self.dato[i,0]
                    self.FiltroActual = self.dato[i,2]
                    self.tamañoActual =self.dato[i,1]
                    self.pixmap1 = self.filtro(self.letra1,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.pixmap2 = self.filtro(self.letra2,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.pixmap3 = self.filtro(self.letra3,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.pixmap4 = self.filtro(self.letra4,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.pixmap5 = self.filtro(self.letra5,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.ui.Foto2.setPixmap(self.pixmap1)
                    self.ui.Foto3.setPixmap(self.pixmap2)
                    self.ui.Foto4.setPixmap(self.pixmap3)
                    self.ui.Foto5.setPixmap(self.pixmap4)
                    self.ui.Foto6.setPixmap(self.pixmap5)
                elif auxResul == 2:
                    self.contrasteActual = self.dato[i, 3]
                    self.FiltroActual = self.dato[i, 5]
                    self.tamañoActual = self.dato[i, 4]
                    self.ui.Foto2.setPixmap(self.filtro(self.letra1, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i,4])))
                    self.ui.Foto3.setPixmap(self.filtro(self.letra2, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))
                    self.ui.Foto4.setPixmap(self.filtro(self.letra3, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))
                    self.ui.Foto5.setPixmap(self.filtro(self.letra4, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))
                    self.ui.Foto6.setPixmap(self.filtro(self.letra5, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))

            elif len(letras) == 3:
                # Cargar letras:
                self.letra1 = 'Sloan2/Sloan_{}.png'.format(letras[0])
                self.letra2 = 'Sloan2/Sloan_{}.png'.format(letras[1])
                self.letra3 = 'Sloan2/Sloan_{}.png'.format(letras[2])
                if auxResul == 1:
                    self.contrasteActual = self.dato[i,0]
                    self.FiltroActual = self.dato[i,2]
                    self.tamañoActual =self.dato[i,1]

                    self.pixmap2 = self.filtro(self.letra1,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.pixmap3 = self.filtro(self.letra2,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.pixmap4 = self.filtro(self.letra3,int(self.dato[i,2]),int(self.dato[i,0]),int(self.dato[i,1]))
                    self.ui.Foto3.setPixmap(self.pixmap2)
                    self.ui.Foto4.setPixmap(self.pixmap3)
                    self.ui.Foto5.setPixmap(self.pixmap4)

                elif auxResul == 2:
                    self.contrasteActual = self.dato[i, 3]
                    self.FiltroActual = self.dato[i, 5]
                    self.tamañoActual = self.dato[i, 4]
                    self.ui.Foto3.setPixmap(self.filtro(self.letra1, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))
                    self.ui.Foto4.setPixmap(self.filtro(self.letra2, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))
                    self.ui.Foto5.setPixmap(self.filtro(self.letra3, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))

        if self.auxEstimulo == "1":
            self.ui.Foto2.setVisible(False)
            self.ui.Foto3.setVisible(False)
            self.ui.Foto4.setVisible(False)
            self.ui.Foto5.setVisible(False)
            self.ui.Foto6.setVisible(False)
            self.letra6 = 'Sloan2/Sloan_{}.png'.format(letras[self.auxEstimuloIndi])
            if auxResul == 1:
                self.contrasteActual = self.dato[i, 0]
                self.FiltroActual = self.dato[i, 2]
                self.tamañoActual = self.dato[i, 1]
                self.ui.Foto1.setPixmap(self.filtro(self.letra6, int(self.dato[i, 2]), int(self.dato[i, 0]), int(self.dato[i, 1])))
            elif auxResul == 2:
                self.contrasteActual = self.dato[i, 3]
                self.FiltroActual = self.dato[i, 5]
                self.tamañoActual = self.dato[i, 4]
                self.ui.Foto1.setPixmap(self.filtro(self.letra6, int(self.dato[i, 5]), int(self.dato[i, 3]), int(self.dato[i, 4])))
            self.timer.setInterval(500)
            self.timer.timeout.connect(self.Limpiar)
            self.timer.start()

    def Limpiar(self) -> None:
        self.ui.Foto1.clear()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() in [Qt.Key.Key_A, Qt.Key.Key_B, Qt.Key.Key_C, Qt.Key.Key_D, Qt.Key.Key_E, Qt.Key.Key_F, Qt.Key.Key_G, Qt.Key.Key_H, Qt.Key.Key_I,
                            Qt.Key.Key_J, Qt.Key.Key_K, Qt.Key.Key_L, Qt.Key.Key_M, Qt.Key.Key_N, Qt.Key.Key_O, Qt.Key.Key_P, Qt.Key.Key_Q, Qt.Key.Key_R,
                            Qt.Key.Key_S, Qt.Key.Key_T, Qt.Key.Key_U, Qt.Key.Key_V, Qt.Key.Key_W, Qt.Key.Key_X, Qt.Key.Key_Y, Qt.Key.Key_Z,Qt.Key.Key_0,Qt.Key.Key_1,
                           Qt.Key.Key_2,Qt.Key.Key_3,Qt.Key.Key_4,Qt.Key.Key_5,Qt.Key.Key_6,Qt.Key.Key_7,Qt.Key.Key_8,Qt.Key.Key_9]:
            letra = event.text().upper()
            self.matriz_letras.append(letra)
            if self.auxEstimulo == "2":
                if len(self.matriz_letras) == len(self.MatrizCorrecta):
                    self.MatrizR.append(self.matriz_letras == self.MatrizCorrecta)
                    resultado = np.sum(np.logical_and(self.MatrizR[self.EstimuloActual], True))
                    auxResultado = [len(self.matriz_letras), resultado, self.contrasteActual, self.FiltroActual,
                                    self.tamañoActual]
                    self.ResultadosPrueba.append(auxResultado)
                    if self.EstimuloActual <= self.maxEstimulos-3:
                        self.EstimuloActual += 1
                        if resultado > len(self.matriz_letras)/2:
                            self.i += 1
                            self.cargarImagenes(self.i,1)

                        elif resultado < len(self.matriz_letras)/2:
                            self.i += 1
                            self.cargarImagenes(self.i, 2)
                    else:
                        print(self.ResultadosPrueba)
                    self.matrz_Coreccta = []
                    self.matriz_letras = []
            elif self.auxEstimulo == "1":
                if self.auxEstimuloIndi <= len(self.MatrizCorrecta)-2:
                    self.auxEstimuloIndi += 1
                    self.cargarImagenes(self.i,self.auxResulIndi)
                else:
                    if len(self.matriz_letras) == len(self.MatrizCorrecta):
                        self.MatrizR.append(self.matriz_letras == self.MatrizCorrecta)
                        resultado = np.sum(np.logical_and(self.MatrizR[self.EstimuloActual], True))
                        auxResultado = [len(self.matriz_letras), resultado, self.contrasteActual, self.FiltroActual,
                                        self.tamañoActual]
                        self.ResultadosPrueba.append(auxResultado)
                        if self.EstimuloActual <= self.maxEstimulos - 3:
                            self.EstimuloActual += 1
                            if resultado > len(self.matriz_letras) / 2:
                                self.i += 1
                                self.auxResulIndi = 1
                                self.auxEstimuloIndi = 0
                                self.cargarImagenes(self.i, 1)
                            elif resultado < len(self.matriz_letras) / 2:
                                self.i += 1
                                self.auxResulIndi = 2
                                self.auxEstimuloIndi = 0
                                self.cargarImagenes(self.i, 2)

                        else:
                            print(self.ResultadosPrueba)
                        self.matrz_Coreccta = []
                        self.matriz_letras = []


    def filtro(self,url,slid,contras,ScaleD):
        img = io.imread(url, as_gray=True)

        sc = min(img.shape)
        img = img[:sc, :sc]

        # Fourier transform
        img_tf = fftpack.fftshift(fftpack.fft2(img))

        # Create circular mask
        center = (img.shape[0] // 2, img.shape[1] // 2)
        r1 = 1  # Inner radius of the bandpass filter
        r2 = slid  # Outer radius of the bandpass filter
        mask = np.zeros(img.shape, dtype=np.uint8)
        rr, cc = draw.disk(center, r2, shape=img.shape)
        mask[rr, cc] = 1
        rr, cc = draw.disk(center, r1, shape=img.shape)
        mask[rr, cc] = 0

        # Apply filter
        tf_filtered = img_tf * mask
        img_filtered = np.real(fftpack.ifft2(fftpack.ifftshift(tf_filtered)))

        # Adjust contrast
        img_contrast = exposure.rescale_intensity(img_filtered, in_range='image', out_range=(contras/100, 0.502))

        img_uint8 = np.clip(img_contrast * 255,0,255).astype(np.uint8)

        h, w = img_uint8.shape

        q_img = QImage(img_uint8.data, w, h, QImage.Format.Format_Grayscale8)

        pixmap = QPixmap.fromImage(q_img).scaled(ScaleD,ScaleD)

        return  pixmap


if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = QGuiApplication.screens()[1]
    mi_app = GuiContraste()
    mi_app.setGeometry(screen.geometry())
    mi_app.show()
    sys.exit(app.exec())