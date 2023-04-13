"""
@author John Harris
"""
import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ApplicationView(QMainWindow):
    
    
    def __init__(self):
        super(ApplicationView, self).__init__()

        # Set up the main window
        self.setWindowTitle("Grid Application")
        self.setGeometry(100, 100, 400, 400)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a grid layout for the central widget
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # Add labels to the grid layout to represent the cells in the 8x8 grid
        for i in range(8):
            for j in range(8):
                label = QLabel(f"({i},{j})")
                label.setAlignment(Qt.AlignCenter)
                grid_layout.addWidget(label, i, j)

        # Add some spacing to the grid layout
        grid_layout.setHorizontalSpacing(10)
        grid_layout.setVerticalSpacing(10)

        # Adjust the size of the labels to fit the cells in the grid
        for i in range(8):
            grid_layout.setColumnStretch(i, 1)
            grid_layout.setRowStretch(i, 1)