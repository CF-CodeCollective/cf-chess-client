from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    """Main Window."""
    '''
    -1 is default value
    1 is player vs player
    2 is player vs cpu
    
    Depending on what button you click it will change this numbers value
    '''
    play_status = -1

    def createMenuBar(self):
        # Added Buttons here to try and make a more complete screen with options that could be used in the future
        menuBar = self.menuBar()
        logInMenu = menuBar.addMenu("&Log In")
        helpMenu = menuBar.addMenu("&Help")

    def uiComponents(self):
        # creating a push button
        startButton = QPushButton("Player vs Player", self)
        # setting geometry of button
        startButton.setGeometry(50, 300, 300, 60)
        # adding action to a button
        startButton.clicked.connect(self.actiononClick)

    def actiononClick(self):
        # printing pressed
        # Need to add link to start main game pointing to a print statement till I find a way to launch. -BF
        print("Player vs Player selected")
        self.play_status = 1
        self.close()

    def value(self):
        return self.play_status

    # Launches Menu screen pointed at self
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Code Collective Chess Team")
        self.resize(800, 400)
        self.centralWidget = QLabel("Welcome to The Chess Project!")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self.createMenuBar()
        self.uiComponents()


# Creates the instance of the window and menu.
class StartMenu:
    def start(self):
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        app.exec_()
        return win.value()

    def get_value(self):
        print("Hello")
