from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    """Main Window."""

    def createMenuBar(self):
        # Added Buttons here to try and make a more complete screen with options that could be used in the future
        menuBar = self.menuBar()
        logInMenu = menuBar.addMenu("&Log In")
        helpMenu = menuBar.addMenu("&Help")

    def UiComponents(self):
        # creating a push button
<<<<<<< HEAD
        startButton = QPushButton("Click To Play", self)
        # setting geometry of button
        startButton.setGeometry(200, 150, 100, 30)
        # adding action to a button
        startButton.clicked.connect(self.clickAction)
=======
        button = QPushButton("Click To Play", self)
        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)
        # adding action to a button
        button.clicked.connect(self.clickAction)
>>>>>>> origin/master

    def clickAction(self):
        # printing pressed
        # Need to add link to start main game pointing to a print statement till I find a way to launch. -BF
        print("Game Started")

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
        self.UiComponents()


# Creates the instance of the window and menu.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
