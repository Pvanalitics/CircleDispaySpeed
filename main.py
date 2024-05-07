import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import QPoint

# Constants
WIDTH, HEIGHT = 450, 450
CIRCLE_RADIUS = 15
TEXT_FONT_SIZE = 50
PROFILE_FONT_SIZE = 20
DISTANCE_FONT_SIZE = 35

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AkaDisp_v0.1')
        self.setGeometry(100, 100, WIDTH, HEIGHT)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(20, 20, 20))
        self.setPalette(p)

    def paint_event(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.draw_circle(painter)
        self.draw_text(painter)
        self.draw_profile(painter)
        self.draw_line(painter)
        self.draw_distance(painter)

    def draw_circle(self, painter):
        pen_circle = QPen(QColor(0, 255, 0), CIRCLE_RADIUS)
        painter.setPen(pen_circle)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawEllipse(CIRCLE_RADIUS, CIRCLE_RADIUS, WIDTH - 2 * CIRCLE_RADIUS, HEIGHT - 2 * CIRCLE_RADIUS)

    def draw_text(self, painter):
        font = QFont('NHL Calgary', TEXT_FONT_SIZE)
        painter.setFont(font)
        pen_text = QPen(QColor(255, 255, 255))
        painter.setPen(pen_text)
        text = '30 km/h'
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        center_x = int((WIDTH - text_width) / 2)
        center_y = int((HEIGHT + text_height) / 2)
        center_point = QPoint(center_x, center_y)
        painter.drawText(center_point, text)

    def draw_profile(self, painter):
        profile_font = QFont('Arial', PROFILE_FONT_SIZE)
        painter.setFont(profile_font)
        profile_text = 'NORMAL'
        profile_text_width = painter.fontMetrics().width(profile_text)
        profile_center_x = int((WIDTH - profile_text_width) / 2)
        profile_center_y = int(center_y - text_height - 30)
        profile_point = QPoint(profile_center_x, profile_center_y)
        painter.drawText(profile_point, profile_text)

    def draw_line(self, painter):
        line_y = int(center_y - text_height - 20)
        painter.drawLine(200, line_y, 250, line_y)

    def draw_distance(self, painter):
        distance_font = QFont('Arial', DISTANCE_FONT_SIZE)
        painter.setFont(distance_font)
        distance_text = '0:10 min'
        distance_text_width = painter.fontMetrics().width(distance_text)
        distance_center_x = int((WIDTH - distance_text_width) / 2)
        distance_center_y = int(center_y + text_height + 10)
        distance_point = QPoint(distance_center_x, distance_center_y)
        painter.drawText(distance_point, distance_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.showFullScreen()  # <--- Make the window full screen
    sys.exit(app.exec_())