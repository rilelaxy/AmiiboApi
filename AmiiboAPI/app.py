import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QHBoxLayout, QGridLayout, QFrame
from PyQt6.QtGui import QIcon, QImage, QPixmap
from PyQt6.QtCore import Qt
import controller

class AmiiboApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open("AmiiboAPI/styles.qss").read())

        self.setWindowTitle("Amiibo Finder")
        self.setWindowIcon(QIcon("AmiiboAPI/icon.png"))
        self.setGeometry(900, 300, 300, 600)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        self.logo = QLabel(self)
        image = QImage("AmiiboAPI/icon.png")
        pixmap = QPixmap.fromImage(image).scaledToWidth(80)
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.logo)

        # Welcome message
        self.welcome = QLabel("Welcome\nto Amiibo Finder")
        self.welcome.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.welcome)

        # Search input and button
        search_layout = QHBoxLayout()
        self.amiibo_name_input = QLineEdit()
        self.amiibo_name_input.setPlaceholderText("Enter Amiibo")
        search_layout.addWidget(self.amiibo_name_input)
        self.search_button = QPushButton("⌕")
        self.search_button.clicked.connect(self.search_amiibo)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        # Categories
        self.categories_label = QLabel("Categories")
        self.categories_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.categories_label)

        # Series
        series_frame = QFrame()
        series_frame.setObjectName('whiteBox')
        series_layout = QVBoxLayout()
        series_frame.setLayout(series_layout)
        self.series_label = QLabel("Series")
        self.series_value = QLabel("")
        series_layout.addWidget(self.series_label)
        series_layout.addWidget(self.series_value)
        layout.addWidget(series_frame)

        # Release
        release_frame = QFrame()
        release_frame.setObjectName('whiteBox')
        release_layout = QVBoxLayout()
        release_frame.setLayout(release_layout)
        self.release_label = QLabel("Release")
        self.release_value = QLabel("")
        release_layout.addWidget(self.release_label)
        release_layout.addWidget(self.release_value)
        layout.addWidget(release_frame)

        # Name
        name_frame = QFrame()
        name_frame.setObjectName('whiteBox')
        name_layout = QVBoxLayout()
        name_frame.setLayout(name_layout)
        self.name_label = QLabel("Name")
        self.name_value = QLabel("")
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_value)
        layout.addWidget(name_frame)

        # Top Amiibo
        self.top_amiibo_label = QLabel("Top Amiibo")
        self.top_amiibo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.top_amiibo_label)

        top_amiibo_frame = QFrame()
        top_amiibo_frame.setObjectName('whiteBox')
        top_amiibo_layout = QVBoxLayout()
        top_amiibo_frame.setLayout(top_amiibo_layout)

        self.top_amiibo1 = QLabel("Link\nLegend of Zelda")
        self.top_amiibo1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        top_amiibo_layout.addWidget(self.top_amiibo1)

        self.top_amiibo2 = QLabel("Mario\nSuper Mario Bros.")
        self.top_amiibo2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        top_amiibo_layout.addWidget(self.top_amiibo2)

        layout.addWidget(top_amiibo_frame)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def search_amiibo(self):
        amiibo_name = self.amiibo_name_input.text()
        controller.search_amiibo(amiibo_name, self)

def main():
    app = QApplication(sys.argv)
    amiibo_app = AmiiboApp()
    amiibo_app.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
