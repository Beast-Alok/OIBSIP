from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from apikey import apikey

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 752)
        MainWindow.setStyleSheet("background-color: rgb(20, 20, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);\n"
"background-color: rgb(40, 40, 40);\n"
"border-radius:15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_country = QtWidgets.QLabel(self.frame_3)
        self.label_country.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_country.setText("")
        self.label_country.setObjectName("label_country")
        self.gridLayout.addWidget(self.label_country, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_city = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_city.sizePolicy().hasHeightForWidth())
        self.lineEdit_city.setSizePolicy(sizePolicy)
        self.lineEdit_city.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_timezone = QtWidgets.QLabel(self.frame_3)
        self.label_timezone.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_timezone.setText("")
        self.label_timezone.setObjectName("label_timezone")
        self.gridLayout.addWidget(self.label_timezone, 3, 1, 1, 1)
        self.label_region = QtWidgets.QLabel(self.frame_3)
        self.label_region.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_region.setText("")
        self.label_region.setObjectName("label_region")
        self.gridLayout.addWidget(self.label_region, 1, 1, 1, 1)
        self.label_localtime = QtWidgets.QLabel(self.frame_3)
        self.label_localtime.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_localtime.setText("")
        self.label_localtime.setObjectName("label_localtime")
        self.gridLayout.addWidget(self.label_localtime, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 89))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_windspeed = QtWidgets.QLabel(self.frame_4)
        self.label_windspeed.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_windspeed.setText("")
        self.label_windspeed.setObjectName("label_windspeed")
        self.gridLayout_3.addWidget(self.label_windspeed, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_winddir = QtWidgets.QLabel(self.frame_4)
        self.label_winddir.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_winddir.setText("")
        self.label_winddir.setObjectName("label_winddir")
        self.gridLayout_3.addWidget(self.label_winddir, 3, 1, 1, 1)
        self.label_condition = QtWidgets.QLabel(self.frame_4)
        self.label_condition.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_condition.setText("")
        self.label_condition.setObjectName("label_condition")
        self.gridLayout_3.addWidget(self.label_condition, 1, 1, 1, 1)
        self.label_humidity = QtWidgets.QLabel(self.frame_4)
        self.label_humidity.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_humidity.setText("")
        self.label_humidity.setObjectName("label_humidity")
        self.gridLayout_3.addWidget(self.label_humidity, 4, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame_4)
        self.label_27.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 4, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame_4)
        self.label_28.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 0, 1, 1)
        self.label_temp = QtWidgets.QLabel(self.frame_4)
        self.label_temp.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(220, 220, 220);")
        self.label_temp.setText("")
        self.label_temp.setObjectName("label_temp")
        self.gridLayout_3.addWidget(self.label_temp, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_find_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_find_2.setMinimumSize(QtCore.QSize(132, 0))
        self.pushButton_find_2.setMaximumSize(QtCore.QSize(133, 40))
        self.pushButton_find_2.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;")
        self.pushButton_find_2.setObjectName("pushButton_find_2")
        self.horizontalLayout_2.addWidget(self.pushButton_find_2)
        self.pushButton_find = QtWidgets.QPushButton(self.frame)
        self.pushButton_find.setMinimumSize(QtCore.QSize(132, 0))
        self.pushButton_find.setMaximumSize(QtCore.QSize(133, 40))
        self.pushButton_find.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;")
        self.pushButton_find.setObjectName("pushButton_find")
        self.horizontalLayout_2.addWidget(self.pushButton_find)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_find_2.clicked.connect(self.method_clear)
        self.pushButton_find.clicked.connect(self.method_find)

    def method_clear(self):
        self.lineEdit_city.clear()
        self.label_region.clear()
        self.label_country.clear()
        self.label_timezone.clear()
        self.label_localtime.clear()
        self.label_temp.clear()
        self.label_condition.clear()
        self.label_windspeed.clear()
        self.label_winddir.clear()
        self.label_humidity.clear()

    def method_find(self):
        city = self.lineEdit_city.text()
        base_url = 'http://api.weatherapi.com/v1/current.json'

        params = {
                'key':apikey,
                'q':city
        }

        response = requests.get(base_url,params=params)

        if response.status_code == 200:
                data = response.json()
                self.label_region.setText(data['location']['region'])
                self.label_country.setText(data['location']['country'])
                self.label_timezone.setText(data['location']['tz_id'])
                self.label_localtime.setText(data['location']['localtime'])
                self.label_temp.setText(str(data['current']['temp_c']))
                self.label_condition.setText(data['current']['condition']['text'])
                self.label_windspeed.setText(str(data['current']['wind_kph']))
                self.label_winddir.setText(data['current']['wind_dir'])
                self.label_humidity.setText(str(data['current']['humidity']))

        else:
                self.lineEdit_city.clear()
                self.label_region.setText("Failed to fetch data")
                self.label_country.setText("Failed to fetch data")
                self.label_timezone.setText("Failed to fetch data")
                self.label_localtime.setText("Failed to fetch data")
                self.label_temp.setText("Failed to fetch data")
                self.label_condition.setText("Failed to fetch data")
                self.label_windspeed.setText("Failed to fetch data")
                self.label_winddir.setText("Failed to fetch data")
                self.label_humidity.setText("Failed to fetch data")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App By Alok"))
        self.label.setText(_translate("MainWindow", "Weather App"))
        self.label_3.setText(_translate("MainWindow", "Region"))
        self.label_4.setText(_translate("MainWindow", "Country"))
        self.lineEdit_city.setPlaceholderText(_translate("MainWindow", "Enter city name"))
        self.label_5.setText(_translate("MainWindow", "Time Zone"))
        self.label_6.setText(_translate("MainWindow", "Local Time"))
        self.label_2.setText(_translate("MainWindow", "City"))
        self.label_21.setText(_translate("MainWindow", "Condition"))
        self.label_22.setText(_translate("MainWindow", "Wind Speed (kph)"))
        self.label_23.setText(_translate("MainWindow", "Wind Direction"))
        self.label_27.setText(_translate("MainWindow", "Humidity"))
        self.label_28.setText(_translate("MainWindow", "Temperature (*C)      "))
        self.pushButton_find_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_find.setText(_translate("MainWindow", "Find"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
