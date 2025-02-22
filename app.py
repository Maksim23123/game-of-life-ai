import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        window = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout()
        
        self._init_canvas_holder()
        self._init_gui_elements()
        self._init_timer()

        window.setLayout(self.main_layout)
        self.setCentralWidget(window)
    
    
    def _init_canvas_holder(self):
        self.canvas_holder = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.canvas_holder.setPixmap(canvas)
        self.setCentralWidget(self.canvas_holder)
        self.draw_something()
    
    
    def _init_gui_elements(self):
        control_panel_layout = QtWidgets.QVBoxLayout()
        
        self.start_button = QtWidgets.QPushButton("Start")
        self.stop_button = QtWidgets.QPushButton("Stop")
        
        self.x = 1
        self.test_label = QtWidgets.QLabel()
        self.test_label.setText(str(self.x))
        
        control_panel_layout.addWidget(self.start_button)
        control_panel_layout.addWidget(self.stop_button)
        control_panel_layout.addWidget(self.test_label)
        
        self.main_layout.addLayout(control_panel_layout)
        self.main_layout.addWidget(self.canvas_holder)
        

    def _init_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1)
    
    
    def update(self):
        self.x += 1
        self.test_label.setText(str(self.x))

    def draw_something(self):
        canvas = self.canvas_holder.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
        self.canvas_holder.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()