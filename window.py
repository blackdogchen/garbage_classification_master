from PySide2.QtWidgets import QApplication,QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QTimer
from PySide2.QtGui import QImage, QPixmap
import cv2

class Predictor():
    def __init__(self):
        file = QFile("./UI/main.ui")
        file.open(QFile.ReadOnly)
        file.close()
        self.ui = QUiLoader().load(file)

        self.ui.bnt_load_image.clicked.connect(self.Load)

    def Load(self):
        self.imgNamepath, self.imgType = QFileDialog.getOpenFileName(self.ui,"选择图片",
                                                       "D:/Shetuan/resnet garbage/data/test/Recyclable garbage/" , "*.png")
        img = QPixmap(self.imgNamepath).scaled(self.ui.lb_Image.width(), self.ui.lb_Image.height())
        self.ui.lb_Image.setPixmap(img)

        return self.imgNamepath




if __name__ == '__main__':
    app = QApplication([])
    Predictor = Predictor()
    Predictor.ui.show()
    app.exec_()