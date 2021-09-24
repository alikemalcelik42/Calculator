from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# Hesap Makinesi

class Window(QWidget):
    def __init__(self, title, shape, icon):
        super().__init__()
        self.title = title
        self.x, self.y, self.w, self.h = shape
        self.operation = ""
        self.resultFinded = False
        self.vbox = QVBoxLayout()
        self.icon = QIcon(icon)
        self.setLayout(self.vbox)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowIcon(self.icon)
        self.setFont(QFont("Arial", 11))

        self.operation_label = QLabel(text=self.operation)
        self.vbox.addWidget(self.operation_label)

        self.result_text = QLineEdit()
        self.vbox.addWidget(self.result_text)

        grid = QGridLayout()
        grid.addWidget(QPushButton(text="C", clicked=self.PressClear), 0, 0)
        grid.addWidget(QPushButton(text="Del", clicked=self.PressDelete), 0, 1)
        grid.addWidget(QPushButton(text="=", clicked=self.PressResult), 0, 2)
        grid.addWidget(QPushButton(text="+", clicked=lambda : self.PressOpr("+")), 0, 3)
        grid.addWidget(QPushButton(text="1", clicked=lambda : self.PressNumber("1")))
        grid.addWidget(QPushButton(text="2", clicked=lambda : self.PressNumber("2")))
        grid.addWidget(QPushButton(text="3", clicked=lambda : self.PressNumber("3")))
        grid.addWidget(QPushButton(text="-", clicked=lambda : self.PressOpr("-")))
        grid.addWidget(QPushButton(text="4", clicked=lambda : self.PressNumber("4")))
        grid.addWidget(QPushButton(text="5", clicked=lambda : self.PressNumber("5")))
        grid.addWidget(QPushButton(text="6", clicked=lambda : self.PressNumber("6")))
        grid.addWidget(QPushButton(text="x", clicked=lambda : self.PressOpr("*")))
        grid.addWidget(QPushButton(text="7", clicked=lambda : self.PressNumber("7")))
        grid.addWidget(QPushButton(text="8", clicked=lambda : self.PressNumber("8")))
        grid.addWidget(QPushButton(text="9", clicked=lambda : self.PressNumber("9")))
        grid.addWidget(QPushButton(text="÷", clicked=lambda : self.PressOpr("/")))
        grid.addWidget(QPushButton(text="0", clicked=lambda : self.PressNumber("0")))
        grid.addWidget(QPushButton(text=".", clicked=lambda : self.PressNumber(".")))
        grid.addWidget(QPushButton(text="(", clicked=lambda : self.PressNumber("(")))
        grid.addWidget(QPushButton(text=")", clicked=lambda : self.PressNumber(")")))
        self.vbox.addLayout(grid)
        self.vbox.addStretch()

    def PressNumber(self, key):
        if self.resultFinded:
            self.PressClear()
            self.resultFinded = False
        self.result_text.setText(self.result_text.text() + key)
        self.operation += key
        self.operation_label.setText(self.operation.replace("*", "x").replace("/", "÷"))

    def PressOpr(self, key):
        if self.resultFinded:
            self.resultFinded = False
        self.result_text.setText("")
        self.operation += key
        self.operation_label.setText(self.operation.replace("*", "x").replace("/", "÷"))

    def PressResult(self):
        result = eval(self.operation)
        self.result_text.setText(str(result))
        self.operation_label.setText(self.operation.replace("*", "x").replace("/", "÷") + "=")
        self.operation_label.setText(self.operation.replace("*", "x").replace("/", "÷") + "=")
        self.operation = str(result)
        self.resultFinded = True

    def PressClear(self):
        self.result_text.setText("")
        self.operation = ""
        self.operation_label.setText("")

    def DeleteLastLetter(self, text):
        deletedText = text.rstrip(text[-1])
        return deletedText

    def PressDelete(self):
        if self.result_text.text() != "":
            self.result_text.setText(self.DeleteLastLetter(self.result_text.text()))
            self.operation = self.DeleteLastLetter(self.operation)
            self.operation_label.setText(self.DeleteLastLetter(self.operation_label.text()))
            print(self.operation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window("Calculator", (200, 200, 0, 0), "../img/icon.jpg")
    app.setStyle("Windows")
    app.exec_()
