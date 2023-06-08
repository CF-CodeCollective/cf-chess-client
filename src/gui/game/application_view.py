import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt


class BoardApplication(QMainWindow):
    def __init__(self):
        super(BoardApplication, self).__init__()

        # Set up the main window
        self.setWindowTitle("Chess Board")
        self.setGeometry(100, 100, 800, 800)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a grid layout for the central widget
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # Add labels to the grid layout to represent the cells in the 8x8 grid
        for i in range(8):
            for j in range(8):
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)
                label.setFixedSize(100, 100)  # Set fixed size for each cell
                label.setStyleSheet("border: 1px solid black")  # Add border to each cell
                grid_layout.addWidget(label, i, j)

        grid_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # Add some spacing to the grid layout
        grid_layout.setHorizontalSpacing(1)
        grid_layout.setVerticalSpacing(1)

        # Adjust the size of the labels to fit the cells in the grid
        for i in range(8):
            grid_layout.setColumnStretch(i, 1)
            grid_layout.setRowStretch(i, 1)

        # Show the main window
        self.show()