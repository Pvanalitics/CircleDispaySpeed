import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import QPoint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AkaDisp_v0.1')
        self.setGeometry(100, 100, 450, 450)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(20, 20, 20))
        self.setPalette(p)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Рисуем круг с обводкой зеленого цвета
        pen_circle = QPen(QColor(0, 255, 0), 15)
        painter.setPen(pen_circle)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawEllipse(15, 15, 420, 420)

        # Рисуем текст белого цвета
        font = QFont('NHL Calgary', 50)
        painter.setFont(font)
        pen_text = QPen(QColor(255, 255, 255))
        painter.setPen(pen_text)
        text = '30 km/h'
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        center_x = int((self.width() - text_width) / 2)
        center_y = int((self.height() + text_height) / 2)
        center_point = QPoint(center_x, center_y)
        painter.drawText(center_point, text)

        # Рисуем надпись "Profile"
        profile_font = QFont('Arial', 20)
        painter.setFont(profile_font)
        profile_text = 'NORMAL'
        profile_text_width = painter.fontMetrics().width(profile_text)
        profile_center_x = int((self.width() - profile_text_width) / 2)
        profile_center_y = int(center_y - text_height - 30)  # Располагаем надпись выше скорости
        profile_point = QPoint(profile_center_x, profile_center_y)
        painter.drawText(profile_point, profile_text)

        # Рисуем линию
        line_y = int(center_y - text_height - 20)  # Располагаем линию между текстом и скоростью
        painter.drawLine(200, line_y, 250, line_y)  # Рисуем линию от (200, line_y) до (250, line_y)

        # Рисуем надпись "0:10m"
        distance_font = QFont('Arial', 35)
        painter.setFont(distance_font)
        distance_text = '0:10 min'
        distance_text_width = painter.fontMetrics().width(distance_text)
        distance_center_x = int((self.width() - distance_text_width) / 2)
        distance_center_y = int(center_y + text_height + 10)  # Располагаем надпись ниже скорости
        distance_point = QPoint(distance_center_x, distance_center_y)
        painter.drawText(distance_point, distance_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
