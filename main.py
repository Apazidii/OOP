import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import os
import classes
import design  # Это наш конвертированный файл дизайна
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.CreateButton.clicked.connect(self.New_Plan)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки

    def New_Plan(self):

        #Получаем данные о времени заметки из InputDate
        Date = self.InputDate.date().toString()
        Time = self.InputDate.time().toString()

        #Получаем данные о важности заметок
        Importance = "LowWarring"
        if self.radioButtonWarring.isChecked():
            importance = "LotWarring"
        elif self.radioButtonMiddle.isChecked():
            importance = "MiddleWarring"
        elif self.radioButtonNoWarring.isChecked():
            importance = "LowWarring"

        #Получаем данные о периоде напоминаний
        Period = "OneTime"
        if self.RButtinEveryDay.isChecked():
            Period= "EveryDay"
        elif self.RButtinEveryWeek.isChecked():
            Period = "EveryWeek"
        elif self.RButtinEveryMouth.isChecked():
            Period = "EveryMouth"
        elif self.RButtonOneTime.isChecked():
            Period = "OneTime"

        StopPeriod = self.LimitDate.date().toString()
        Text = self.NewText.toPlainText()

        print(Date,Time,Importance,Period,StopPeriod,Text,sep=",")

        newPlan = classes.Plan(Date,Time,Importance,Period,StopPeriod,Text)
        newPlan.toJSON()












def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
