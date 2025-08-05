import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QBuffer, QByteArray

class RadarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live NY Doppler Radar")
        self.setFixedSize(600, 600)

        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(600, 600)

        # ✅ Download latest radar loop GIF from NWS
        gif_url = "https://radar.weather.gov/ridge/standard/NORTHEAST_loop.gif"
        response = requests.get(gif_url)
        if response.status_code != 200:
            print("❌ Failed to download radar GIF.")
            return

        gif_bytes = QByteArray(response.content)

        # ✅ Load GIF into QMovie via QBuffer
        self.buffer = QBuffer()
        self.buffer.setData(gif_bytes)
        self.buffer.open(QBuffer.ReadOnly)

        movie = QMovie()
        movie.setDevice(self.buffer)
        movie.setScaledSize(self.label.size())

        if not movie.isValid():
            print("❌ Invalid GIF format.")
            return

        self.label.setMovie(movie)
        movie.start()

        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadarWindow()
    window.show()
    sys.exit(app.exec_())