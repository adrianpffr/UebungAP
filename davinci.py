import math

import PyQt6
from PyQt6.QtCore import Qt, QRectF, QPointF, QSize
from PyQt6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen, QColor, QFont, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel


class DaVinci(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 500) # Setzt die Bildbreite auf 600 und Bildhöhe auf 500
        self.setWindowTitle('DaVinci')
        self.setAutoFillBackground(True) # Stellt sicher, dass der Hintergrund gefüllt wird
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("lightgoldenrodyellow")) # Setzt die Hintergrundfarbe auf lightgoldenrodyellow
        self.setPalette(p)

        # Laden des Bildes und Festlegen der Bildgröße
        self.image = QPixmap('mensch.jpg')
        self.image_size = QSize(400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen()
        painter.setFont(Qt.font('SansSerif', 20))
        painter.drawText(self.rect(), Qt.AlignCenter, 'Hello, DaVinci!')

        # Zeichnen des Titels "Vitruvianischer Mensch" in der rechten oberen Ecke des Bildes
        font = QFont('OldEnglish', 24)
        painter.setFont(font)
        title = 'Vitruvianischer Mensch'
        title_width = painter.fontMetrics().width(title)
        painter.drawText(self.width()-title_width-25, 25+font.pointSize(), title)

        # Zeichnen des Künstlernamens "Leonardo da Vinci" in der rechten oberen Ecke des Bildes
        font = QFont('OldEnglish', 12)
        painter.setFont(font)
        artist = 'Leonardo da Vinci'
        artist_width = painter.fontMetrics().width(artist)
        painter.drawText(self.width()-artist_width-25, 25+font.pointSize()*3, artist)

        pen = QPen(QColor("lightslategray"))
        pen.setWidth(10)
        painter.setPen(pen)

        # Zeichnen des Kreises
        r = 125 # Radius des Kreises
        x = self.width()/2
        y = 25 + r
        painter.drawEllipse(x-r, y-r, 2*r, 2*r)

        # Berechnen der Seitenlänge des Quadrats
        side_length = r * math.sqrt(2)

        # Berechnen der Koordinaten der oberen linken Ecke des Quadrats
        x1 = x - side_length/2
        y1 = y - side_length/2

        # Zeichnen des Quadrats
        painter.drawRect(x1, y1, side_length, side_length)

        # Skalieren und Positionieren des Bildes
        image_rect = QRectF(QPointF(x-self.image_size.width()/2, y+self.image_size.height()/2+25), self.image_size)
        painter.drawPixmap(image_rect, self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.update()

