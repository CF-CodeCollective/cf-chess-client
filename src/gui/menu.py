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

    def createButtons(self):
        # Create "Player vs Player" button
        btn_pvp = QPushButton("Player vs Player", self)
        btn_pvp.setGeometry(250, 150, 300, 50)
        btn_pvp.clicked.connect(self.clickActionPVP)

        # Create "Player vs AI" button
        btn_pva = QPushButton("Player vs AI", self)
        btn_pva.setGeometry(250, 250, 300, 50)
        btn_pva.clicked.connect(self.clickActionPVAI)

    def clickActionPVP(self):
        # printing pressed
        # Need to add link to start main game pointing to a print statement till I find a way to launch. -BF
        print("Player vs Player selected")
        self.play_status = 1
        self.close()

    def clickActionPVAI(self):
        # printing pressed
        # Need to add link to start main game pointing to a print statement till I find a way to launch. -BF
        print("Player vs Player selected")
        self.play_status = 2
        self.close()

    def value(self):
        return self.play_status

    # Launches Menu screen pointed at self
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Code Collective Chess Team")
        self.resize(800, 400)
        label = QLabel("Welcome to The Chess Project!", self)
        label.setGeometry(0, 50, 800, 50)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.createMenuBar()
        self.createButtons()


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
