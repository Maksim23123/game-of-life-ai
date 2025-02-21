import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        window = QtWidgets.QWidget()
        main_layout =QtWidgets.QHBoxLayout()
        
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
        
        control_panel_layout = QtWidgets.QVBoxLayout()
        
        
        self.start_button = QtWidgets.QPushButton("Start")
        self.stop_button = QtWidgets.QPushButton("Stop")
        
        self.x = 1
        self.test_label = QtWidgets.QLabel()
        self.test_label.setText(str(self.x))
        
        control_panel_layout.addWidget(self.start_button)
        control_panel_layout.addWidget(self.stop_button)
        control_panel_layout.addWidget(self.test_label)
        
        main_layout.addLayout(control_panel_layout)
        main_layout.addWidget(self.label)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        window.setLayout(main_layout)
        self.setCentralWidget(window)
    
    
    def update(self):
        self.x += 1
        self.test_label.setText(str(self.x))
        

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()