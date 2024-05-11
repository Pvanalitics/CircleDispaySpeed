import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import QRectF

# Constants
CIRCLE_PADDING = 15
MAX_FONT_SIZE_RATIO = 0.1
PROFILE_FONT_SIZE_RATIO = 0.05
DISTANCE_FONT_SIZE_RATIO = 0.05  # Установим размер меньше, чтобы был чем у '30 km/h'

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AkaDisp_v0.1')
        self.setGeometry(100, 100, 450, 450)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(20, 20, 20))
        self.setPalette(palette)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Calculate the maximum possible size for the circle
        circle_size = min(self.width() - CIRCLE_PADDING * 2, self.height() - CIRCLE_PADDING * 2)

        # Draw circle with green outline
        green_pen = QPen(QColor(0, 255, 0), CIRCLE_PADDING)
        painter.setPen(green_pen)
        painter.setBrush(QColor(0, 0, 0))
        circle_rect = QRectF(CIRCLE_PADDING, (self.height() - circle_size) // 2, circle_size, circle_size)
        painter.drawEllipse(circle_rect)

        # Calculate font size based on the size of the circle and the length of the text
        max_font_size = int(circle_size * MAX_FONT_SIZE_RATIO)

        # Draw text '30 km/h'
        text = '30 km/h'
        font = QFont('NHL Calgary', max_font_size)
        painter.setFont(font)
        white_pen = QPen(QColor(255, 255, 255))
        painter.setPen(white_pen)
        font_metrics = QFontMetrics(font)
        text_width = font_metrics.width(text)
        text_height = font_metrics.height()
        center_x = (self.width() - text_width) // 2
        center_y = (self.height() + text_height) // 2
        painter.drawText(center_x, center_y, text)

        # Draw profile text 'NORMAL'
        profile_text = 'NORMAL'
        profile_font_size = int(max_font_size * PROFILE_FONT_SIZE_RATIO)
        profile_font = QFont('Arial', profile_font_size)
        painter.setFont(profile_font)
        white_pen = QPen(QColor(255, 255, 255))
        painter.setPen(white_pen)
        profile_text_width = font_metrics.width(profile_text)
        profile_center_x = (self.width() - profile_text_width) // 2
        profile_center_y = center_y - text_height - CIRCLE_PADDING
        painter.drawText(profile_center_x, profile_center_y, profile_text)

        # Draw distance text '0:10 min'
        distance_text = '0:10 min'
        distance_font_size = int(max_font_size * DISTANCE_FONT_SIZE_RATIO)
        distance_font = QFont('Arial', distance_font_size)
        painter.setFont(distance_font)
        white_pen = QPen(QColor(255, 255, 255))
        painter.setPen(white_pen)
        distance_text_width = font_metrics.width(distance_text)
        distance_center_x = (self.width() - distance_text_width) // 2
        distance_center_y = center_y + text_height + CIRCLE_PADDING
        painter.drawText(distance_center_x, distance_center_y, distance_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
