from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import random

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '?']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
choiceArray = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 676)
        MainWindow.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_char = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_char.setMinimumSize(QtCore.QSize(0, 40))
        self.spinBox_char.setMaximumSize(QtCore.QSize(73, 36))
        self.spinBox_char.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_char.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.spinBox_char.setMaximum(100)
        self.spinBox_char.setObjectName("spinBox_char")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_char)
        self.checkBox_lower = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_lower.setMinimumSize(QtCore.QSize(40, 47))
        self.checkBox_lower.setMaximumSize(QtCore.QSize(40, 47))
        self.checkBox_lower.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_lower.setText("")
        self.checkBox_lower.setObjectName("checkBox_lower")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox_lower)
        self.checkBox_symbol = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_symbol.setMinimumSize(QtCore.QSize(40, 47))
        self.checkBox_symbol.setMaximumSize(QtCore.QSize(0, 0))
        self.checkBox_symbol.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_symbol.setText("")
        self.checkBox_symbol.setObjectName("checkBox_symbol")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox_symbol)
        self.checkBox_number = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_number.setMinimumSize(QtCore.QSize(40, 47))
        self.checkBox_number.setMaximumSize(QtCore.QSize(0, 0))
        self.checkBox_number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_number.setText("")
        self.checkBox_number.setObjectName("checkBox_number")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox_number)
        self.checkBox_upper = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_upper.setMinimumSize(QtCore.QSize(40, 47))
        self.checkBox_upper.setMaximumSize(QtCore.QSize(5, 0))
        self.checkBox_upper.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_upper.setStyleSheet("")
        self.checkBox_upper.setText("")
        self.checkBox_upper.setObjectName("checkBox_upper")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_upper)
        self.verticalLayout.addLayout(self.formLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 86))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_clear = QtWidgets.QPushButton(self.frame)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(109, 16777215))
        self.pushButton_clear.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";background-color: rgb(206, 206, 206);border-radius:5px;")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(109, 16777215))
        self.pushButton.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";background-color: rgb(206, 206, 206);border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";background-color: rgb(116, 116, 116);border-radius:15px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_copy = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_copy.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_copy.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pushButton_copy.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";background-color: rgb(206, 206, 206);border-radius:5px;")
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.horizontalLayout_3.addWidget(self.pushButton_copy)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.spinBox_char.valueChanged.connect(self.num_char)
        self.checkBox_upper.stateChanged.connect(self.on_checkbox_upper)
        self.checkBox_lower.stateChanged.connect(self.on_checkbox_lower)
        self.checkBox_symbol.stateChanged.connect(self.on_checkbox_symbol)
        self.checkBox_number.stateChanged.connect(self.on_checkbox_number)
        self.pushButton.clicked.connect(self.genrate)
        self.pushButton_copy.clicked.connect(self.copy)
        self.pushButton_clear.clicked.connect(self.clear)
    
    num_of_char = 0
    def num_char(self, value):
        self.num_of_char = value
        
    def on_checkbox_upper(self):
        if 0 in choiceArray:
            choiceArray.remove(0)
        else:
            choiceArray.append(0)
    def on_checkbox_lower(self):
        if 1 in choiceArray:
            choiceArray.remove(1)
        else:
            choiceArray.append(1)
    def on_checkbox_symbol(self):
        if 2 in choiceArray:
            choiceArray.remove(2)
        else:
            choiceArray.append(2)
    def on_checkbox_number(self):
        if 3 in choiceArray:
            choiceArray.remove(3)
        else:
            choiceArray.append(3)
    
    def genrate(self):
        password = ""
        if self.num_of_char < 8:
            self.label_7.setText("Password lenght must be 8 or more")
        else:
            for i in range(self.num_of_char):
                choice = random.choice(choiceArray)
                match choice:
                    case 0:
                        ch = random.choice(upper)
                        password += ch
                    case 1:
                        ch = random.choice(lower)
                        password += ch
                    case 2:
                        ch = random.choice(symbol)
                        password += ch
                    case 3:
                        ch = random.choice(number)
                        password += ch
            self.label_7.setText(password)

    def copy(self):
        if self.label_7.text() == "Generating area for password":
            pass
        else:
            QApplication.clipboard().setText(self.label_7.text())
    
    def clear(self):
        self.checkBox_upper.setChecked(False)
        self.checkBox_lower.setChecked(False)
        self.checkBox_symbol.setChecked(False)
        self.checkBox_number.setChecked(False)
        self.label_7.setText("Generating area for password")
        self.spinBox_char.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator By Alok"))
        self.label.setText(_translate("MainWindow", "Password Generator"))
        self.label_2.setText(_translate("MainWindow", "Number of Characters       "))
        self.label_3.setText(_translate("MainWindow", "Upper Case Characters     "))
        self.label_4.setText(_translate("MainWindow", "Lower Case Characters     "))
        self.label_5.setText(_translate("MainWindow", "Symbols                           "))
        self.label_6.setText(_translate("MainWindow", "Numbers                          "))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.label_7.setText(_translate("MainWindow", "Generating area for password"))
        self.pushButton_copy.setText(_translate("MainWindow", "Copy Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
