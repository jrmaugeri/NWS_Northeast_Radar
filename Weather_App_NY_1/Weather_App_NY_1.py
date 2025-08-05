import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QSize

class RadarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NY Doppler Radar")
        self.setFixedSize(600, 600)

        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(600, 600)

        # ✅ Load local GIF safely
        gif_path = r"C:\Users\Maugeri\Library\Computers\GIS\Weather_Applications\Weather_Assignment_1\Weather_App_NY_1\NORTHEAST_loop.gif"
        movie = QMovie(gif_path)

        # ✅ Check if movie is valid
        if not movie.isValid():
            print("❌ Failed to load GIF. Check the path or file integrity.")
        else:
            print("✅ GIF loaded successfully.")
            print("Frame count:", movie.frameCount())
            print("Original size:", movie.frameRect().size())

            # Optional: scale the GIF to fit the label
            movie.setScaledSize(QSize(600, 600))

            self.label.setMovie(movie)
            movie.start()

        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadarWindow()
    window.show()
    sys.exit(app.exec_())