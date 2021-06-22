import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from fromFile import *
import testdesign  # Это наш конвертированный файл дизайна


k = 3




class ExampleApp(QtWidgets.QMainWindow, testdesign.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.pushButton.clicked.connect(self.Push2)
        self.pushButton_2.clicked.connect(self.Push)
        self.toolButton.clicked.connect(self.Dele)

    def Push(self):
        global k
        self.NewLabel(k)
        k+=1

    def Push2(self):
        self.label_2.setText("1q2w3e4r")

    def Dele(self):
        self.verticalLayout_2.setEnabled(False)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
