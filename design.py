# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.New = QtWidgets.QWidget()
        self.New.setObjectName("New")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.New)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.New)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.InputDate = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.InputDate.setObjectName("InputDate")
        self.horizontalLayout_5.addWidget(self.InputDate)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.New)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonNoWarring = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonNoWarring.setObjectName("radioButtonNoWarring")
        self.horizontalLayout.addWidget(self.radioButtonNoWarring)
        self.radioButtonMiddle = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMiddle.setObjectName("radioButtonMiddle")
        self.horizontalLayout.addWidget(self.radioButtonMiddle)
        self.radioButtonWarring = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonWarring.setObjectName("radioButtonWarring")
        self.horizontalLayout.addWidget(self.radioButtonWarring)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.New)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RButtonOneTime = QtWidgets.QRadioButton(self.groupBox_2)
        self.RButtonOneTime.setObjectName("RButtonOneTime")
        self.horizontalLayout_2.addWidget(self.RButtonOneTime)
        self.RButtonEveryDay = QtWidgets.QRadioButton(self.groupBox_2)
        self.RButtonEveryDay.setObjectName("RButtonEveryDay")
        self.horizontalLayout_2.addWidget(self.RButtonEveryDay)
        self.RButtonEveryWeek = QtWidgets.QRadioButton(self.groupBox_2)
        self.RButtonEveryWeek.setObjectName("RButtonEveryWeek")
        self.horizontalLayout_2.addWidget(self.RButtonEveryWeek)
        self.RButtonEveryMouth = QtWidgets.QRadioButton(self.groupBox_2)
        self.RButtonEveryMouth.setObjectName("RButtonEveryMouth")
        self.horizontalLayout_2.addWidget(self.RButtonEveryMouth)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.New)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LimitDate = QtWidgets.QDateEdit(self.groupBox_3)
        self.LimitDate.setObjectName("LimitDate")
        self.horizontalLayout_3.addWidget(self.LimitDate)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.New)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.NewText = QtWidgets.QPlainTextEdit(self.groupBox_5)
        self.NewText.setPlainText("")
        self.NewText.setObjectName("NewText")
        self.verticalLayout_4.addWidget(self.NewText)
        self.horizontalLayout_7.addWidget(self.groupBox_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.CreateButton = QtWidgets.QPushButton(self.New)
        self.CreateButton.setObjectName("CreateButton")
        self.verticalLayout_3.addWidget(self.CreateButton)
        self.tabWidget.addTab(self.New, "")
        self.View = QtWidgets.QWidget()
        self.View.setObjectName("View")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.View)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.View)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.ViewButton = QtWidgets.QPushButton(self.View)
        self.ViewButton.setObjectName("ViewButton")
        self.verticalLayout.addWidget(self.ViewButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(self.View)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.tabWidget.addTab(self.View, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Load = QtWidgets.QAction(MainWindow)
        self.Load.setObjectName("Load")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.SaveAs = QtWidgets.QAction(MainWindow)
        self.SaveAs.setObjectName("SaveAs")
        self.Create = QtWidgets.QAction(MainWindow)
        self.Create.setObjectName("Create")
        self.menu.addAction(self.Create)
        self.menu.addAction(self.Load)
        self.menu.addAction(self.Save)
        self.menu.addAction(self.SaveAs)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOTKA"+"   -   "+"Новый список задач*"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Укажите дату:"))
        self.groupBox.setTitle(_translate("MainWindow", "Укажите важность:"))
        self.radioButtonNoWarring.setText(_translate("MainWindow", "Не важно"))
        self.radioButtonMiddle.setText(_translate("MainWindow", "Обычно"))
        self.radioButtonWarring.setText(_translate("MainWindow", "Важно"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Укажите периодичность"))
        self.RButtonOneTime.setText(_translate("MainWindow", "Один раз"))
        self.RButtonEveryDay.setText(_translate("MainWindow", "Ежедневно"))
        self.RButtonEveryWeek.setText(_translate("MainWindow", "Еженедельно"))
        self.RButtonEveryMouth.setText(_translate("MainWindow", "Ежемесячно"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Повторять до:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Опишите задачу"))
        self.CreateButton.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.New), _translate("MainWindow", "Добавить"))
        self.ViewButton.setText(_translate("MainWindow", "Показать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.View), _translate("MainWindow", "Просмотр"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.Load.setText(_translate("MainWindow", "Загрузить"))
        self.Save.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Сохранить как"))
        self.SaveAs.setText(_translate("MainWindow", "Сохранить как"))
        self.Create.setText(_translate("MainWindow", "Создать"))
