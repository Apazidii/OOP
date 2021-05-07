import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from fromFile import *
import design  # Это наш конвертированный файл дизайна

arrPlans = []
urlFile = ""

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна




        self.setWindowIcon(QtGui.QIcon("src/LogoIcon.png"))

        #Устанавливает в виджетах ввода даты сегодняшнею дату
        self.LimitDate.setDate(datetime.date.today())
        self.InputDate.setDateTime(datetime.datetime.today())

        #Делает по умолчанию Контейнер с датой окончания повторения невидимым
        self.groupBox_3.setVisible(False)

        self.CreateButton.clicked.connect(self.New_Plan)
        self.SaveAs.triggered.connect(self.SaveAs_File)
        self.Save.triggered.connect(self.Save_File)
        self.Load.triggered.connect(self.Load_File)
        self.ViewButton.clicked.connect(self.View_Plans)

    # Проверка на периодичность
    # Если равна одному разу, то Контейнер с датой окончания повторения исчезает
        self.RButtonOneTime.clicked.connect(self.LimitFVisible)
        self.RButtonEveryDay.clicked.connect(self.LimitTVisible)
        self.RButtonEveryMouth.clicked.connect(self.LimitTVisible)
        self.RButtonEveryWeek.clicked.connect(self.LimitTVisible)


    # Делает контейнер с датой окончание видимым
    def LimitFVisible(self):
        self.groupBox_3.setVisible(False)

    # Делает контейнер с датой окончание невидимым
    def LimitTVisible(self):
        self.groupBox_3.setVisible(True)

    def Load_File(self):

        directory = QtWidgets.QFileDialog.getOpenFileName(self,"Выберите файл",filter="*.apaz")

        self.setWindowTitle(self.windowTitle() +"   -   "+Name_From_Url(directory[0]))
        global urlFile
        urlFile = directory[0]

        global arrPlans
        arrPlans = LoadFile(urlFile).copy()


    def SaveAs_File(self):
        directory = QtWidgets.QFileDialog.getSaveFileName(self,"Выберите файл для сохранения",filter="*.apaz")
        self.setWindowTitle(self.windowTitle() + "   -   " + Name_From_Url(directory[0]))
        global urlFile
        urlFile = directory[0]

        SaveFile(urlFile, arrPlans)
        self.setWindowTitle(self.windowTitle()[:-1])

    def Save_File(self):

        global urlFile
        if urlFile =="":
            directory = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите файл для сохранения", filter="*.apaz")
            self.setWindowTitle(self.windowTitle() + "   -   " + Name_From_Url(directory[0]))

            urlFile = directory[0]

            SaveFile(urlFile, arrPlans)
            if self.windowTitle()[-1:] == "*":
                self.setWindowTitle(self.windowTitle()[:-1])
        else:
            SaveFile(urlFile, arrPlans)
            if self.windowTitle()[-1:] == "*":
                self.setWindowTitle(self.windowTitle()[:-1])



    def New_Plan(self):



        #Получаем данные о времени заметки из InputDate
        Date = self.InputDate.date().toPyDate()
        Time = self.InputDate.time().toPyTime()

        #Получаем данные о важности заметок
        Importance = "LowWarring"
        if self.radioButtonWarring.isChecked():
            Importance = "LotWarring"
        elif self.radioButtonMiddle.isChecked():
            Importance = "MiddleWarring"
        elif self.radioButtonNoWarring.isChecked():
            Importance = "LowWarring"

        #Получаем данные о периоде напоминаний
        Period = "OneTime"
        if self.RButtonEveryDay.isChecked():
            self.LimitDate.setVisible(True)
            Period= "EveryDay"
        elif self.RButtonEveryWeek.isChecked():
            self.LimitDate.setVisible(True)
            Period = "EveryWeek"
        elif self.RButtonEveryMouth.isChecked():
            self.LimitDate.setVisible(True)
            Period = "EveryMouth"
        elif self.RButtonOneTime.isChecked():
            self.LimitDate.setVisible(False)
            Period = "OneTime"

        #Получаем данные о времени окончание повторения заметок
        StopPeriod = self.LimitDate.date().toPyDate()
        #Получаем описание заметки
        Text = self.NewText.toPlainText()

        if Period=="OneTime":
            #Из полученных данных создаем diсt
            NewPlan =  {
                "Date": Date,
                "Time": Time, #datetime.time(2, 36, 25, 851000)
                "Importance":Importance,
                "Period":Period,
                "StopPeriod":StopPeriod,
                "Text":Text
            }

            #Добавляем dict-план в общий массив сохранения
            arrPlans.append(NewPlan)

        else:
            times = Periods(Date,StopPeriod,Period)
            for i in times:
                # Из полученных данных создаем diсt
                NewPlan = {
                    "Date": i,
                    "Time": Time,  # datetime.time(2, 36, 25, 851000)
                    "Importance": Importance,
                    "Period": Period,
                    "StopPeriod": StopPeriod,
                    "Text": Text
                }

                # Добавляем dict-план в общий массив сохранения
                arrPlans.append(NewPlan)



        #отчищаем все поля
        self.NewText.clear()
        self.groupBox_3.setVisible(False)
        self.RButtonOneTime.setChecked(True)
        self.radioButtonNoWarring.setChecked(True)
        self.LimitDate.setDate(datetime.date.today())
        self.InputDate.setDateTime(datetime.datetime.today())

        #Добавляем индикатор несохраненого файла ("*" в оглавление после названия файла)
        if self.windowTitle()[-1:]=="*":
            self.setWindowTitle(self.windowTitle() + "*")




    def View_Plans(self):
        t = self.calendarWidget.selectedDate().toPyDate()

        self.listWidget.clear()
        global arrPlans
        l =len(arrPlans)
        arrPlans = sorted(arrPlans, key=lambda arrPlans: arrPlans["Time"])




        for i in range(0, l):
            if t == arrPlans[i]["Date"]:
                if arrPlans[i]["Importance"] == "LotWarring":
                    item = QtWidgets.QListWidgetItem(arrPlans[i]["Time"].strftime("%H:%M") + " " + arrPlans[i]["Text"])
                    item.setIcon(QtGui.QIcon("src/lot.svg"))
                    self.listWidget.addItem(item)

        for i in range(0,l):
            if t == arrPlans[i]["Date"]:
                if arrPlans[i]["Importance"] == "MiddleWarring":
                    item = QtWidgets.QListWidgetItem(arrPlans[i]["Time"].strftime("%H:%M") + " " + arrPlans[i]["Text"])
                    item.setIcon(QtGui.QIcon("src/middle.svg"))
                    self.listWidget.addItem(item)
        for i in range(0,l):
            if t == arrPlans[i]["Date"]:
                if arrPlans[i]["Importance"] == "LowWarring":
                    item = QtWidgets.QListWidgetItem(arrPlans[i]["Time"].strftime("%H:%M") + " " + arrPlans[i]["Text"])
                    item.setIcon(QtGui.QIcon("src/low.svg"))
                    self.listWidget.addItem(item)

















def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
