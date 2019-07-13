import execute
from PyQt4 import QtGui,QtCore


class RegistrationWindow(QtGui.QMainWindow):
    #Registration window for student registration

    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.text_field = QtGui.QPlainTextEdit(self)
        self.text_field.setMinimumSize (800,600)
        self.text_field.setStyleSheet("background-image: url(test.png);")


        #Creating Registration Window
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Chain Trading Helper")

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(100,30,600,60))
        h.setStyleSheet("QLabel { background-color : black;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("Welcome !")


        #SET OF ENTRIES
        #Taking Student's Name
        l1=QtGui.QLabel(self)
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l1.setGeometry(QtCore.QRect(190,150,130,30))
        l1.setStyleSheet("QLabel { background-color : purple;color :white ; }")
        font=QtGui.QFont("Times",14,QtGui.QFont.Bold)
        l1.setFont(font)
        l1.setText("File Name")

        self.e1=QtGui.QLineEdit(self)
        self.e1.setGeometry(450,150,200,30)
        self.e1.setAlignment(QtCore.Qt.AlignCenter)
        font1=QtGui.QFont("Arial",14)
        self.e1.setFont(font1)

        #Taking Student's Registration Number
        l2=QtGui.QLabel(self)
        l2.setAlignment(QtCore.Qt.AlignCenter)
        l2.setGeometry(QtCore.QRect(190,250,130,30))
        l2.setStyleSheet("QLabel { background-color : purple;color :white ; }")
        l2.setFont(font)
        l2.setText("Strike Price")

        self.e2=QtGui.QLineEdit(self)
        self.e2.setGeometry(450,250,200,30)
        self.e2.setAlignment(QtCore.Qt.AlignCenter)
        self.e2.setFont(font1)

        #Button for clearing fields
        b2=QtGui.QPushButton(self)
        b2.setText("RESET")
        b2.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b2.setGeometry(250,450,100,30)
        b2.setStyleSheet("QPushButton { background-color : red ;color : white ; }")
        b2.clicked.connect(self.erase)

        #Button for submission of data
        b1=QtGui.QPushButton(self)
        b1.setText("SUBMIT")
        b1.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b1.setGeometry(450,450,100,30)
        b1.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b1.clicked.connect(self.submit)



    def erase(self):
        #function for clearing fields and changing to default
        self.e1.setText("")
        self.e2.setText("")

    def submit(self):
        #funcion to run python script

        execute.call_execute(self.e1.text(),self.e2.text())




if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = RegistrationWindow()
    gui.show()
    app.exec_()
