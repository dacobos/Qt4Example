from PyQt4 import QtGui, QtCore
import os
import sys

from externalCode import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self, parent)
        self.central_widget = QtGui.QStackedWidget()
        # Geometry Reference: (Left Margin, Upper Margin, Width, Heigth)
        self.setGeometry(100, 100, 850, 480)
        self.setWindowTitle("Testing PyQt4")
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(),'Images','logo.png')))

        self.setCentralWidget(self.central_widget)

        # Create Home widgets and add to central_widget
        self.home_widget = Home(self)
        self.central_widget.addWidget(self.home_widget)

        # Create Home widgets and add to central_widget
        self.second_widget = Second(self)
        self.central_widget.addWidget(self.second_widget)


        # Set the active widget to home_screen
        self.central_widget.setCurrentWidget(self.home_widget)


        # Main Menu Actions
        # Home Screen
        home_action = QtGui.QAction("&Home Screen", self)
        home_action.setShortcut("Ctrl+H")
        home_action.setStatusTip('Using Home Screen')
        home_action.triggered.connect(self.home_method)

        # Second Screen
        second_action = QtGui.QAction("&Second Screen", self)
        second_action.setShortcut("Ctrl+S")
        second_action.setStatusTip('Using Second Screen')
        second_action.triggered.connect(self.second_method)

        # Main Menu Items
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Home Screen')
        fileMenu.addAction(home_action)
        fileMenu = mainMenu.addMenu('&Second Screen')
        fileMenu.addAction(second_action)

    # Main Menu Methods
    def home_method(self):
        self.central_widget.setCurrentWidget(self.home_widget)

    def second_method(self):
        self.central_widget.setCurrentWidget(self.second_widget)

# Home Screen Class
class Home(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        # Label to present background image
        label = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(os.path.join(os.getcwd(),'Images','background.png'))
        pixmap = pixmap.scaled(920, 1, QtCore.Qt.KeepAspectRatioByExpanding)
        label.setPixmap(pixmap)
        #
        # Label to present text
        newFont = QtGui.QFont("Consolas", 28, QtGui.QFont.Bold)
        label0 = QtGui.QLabel("<Home Screen>", self)
        label0.setObjectName('label0')
        label0.setStyleSheet('QLabel#label0 {color: #f0ffff}')
        label0.setWordWrap(True)
        # Geometry Reference: (Left Margin, Upper Margin, Width, Heigth)
        label0.setGeometry(100, 100, 500, 30)
        label0.setFont(newFont)

# Second Screen Class
class Second(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        label = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(os.path.join(os.getcwd(),'Images','background2.jpg'))
        pixmap = pixmap.scaled(920, 1, QtCore.Qt.KeepAspectRatioByExpanding)
        label.setPixmap(pixmap)

        newFont = QtGui.QFont("Consolas", 28, QtGui.QFont.Bold)
        label0 = QtGui.QLabel("<Second Screen>", self)
        label0.setObjectName('label0')
        label0.setStyleSheet('QLabel#label0 {color: #f0ffff}')
        label0.setWordWrap(True)
        # Geometry Reference: (Left Margin, Upper Margin, Width, Heigth)
        label0.setGeometry(100, 100, 500, 30)
        label0.setFont(newFont)
    #     # Button Example
        button1 = QtGui.QPushButton("External 1",self)
        button1.setGeometry(400, 300, 100, 30)
        button1.clicked.connect(self.callExternal1)
        button2 = QtGui.QPushButton("External 2",self)
        button2.setGeometry(500, 300, 100, 30)
        button2.clicked.connect(self.callExternal2)
        button3 = QtGui.QPushButton("Exit",self)
        button3.setGeometry(600, 300, 100, 30)
        button3.clicked.connect(self.exitApplication)

    def callExternal1(self):
        result = externalMethod1()
        QtGui.QMessageBox.information(self, 'Result', result)

    def callExternal2(self):
        result = externalMethod2()
        QtGui.QMessageBox.information(self, 'Result', result)

    def exitApplication(self):
            choice = QtGui.QMessageBox.question(self, 'ExitApp',
                                                "Exit Application?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                sys.exit()
            else:
                pass


# General Instance Launching the App
app = QtGui.QApplication(sys.argv)
myWindow = MainWindow(None)
myWindow.show()
app.exec_()
