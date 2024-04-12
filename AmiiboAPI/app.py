import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon


class AmiiboApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Amiibo Finder")
        self.setWindowIcon(QIcon("AmiiboAPI\AmiiboAPI\icon.png"))  
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  

        self.amiibo_name_input = QLineEdit()
        self.amiibo_name_input.setPlaceholderText("Enter Amiibo Name")  # Placeholder text
        layout.addWidget(self.amiibo_name_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_amiibo)
        layout.addWidget(self.search_button)

        self.response_label = QLabel()
        layout.addWidget(self.response_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def search_amiibo(self):
        amiibo_name = self.amiibo_name_input.text()
        if not amiibo_name:
            QMessageBox.warning(self, "Warning", "Please enter an Amiibo name.") # Error handling
            return

        url = f"https://www.amiiboapi.com/api/amiibo/?name={amiibo_name}"
        try:
            response = requests.get(url)
            data = response.json()
            if data['amiibo']:
                amiibo_data = data['amiibo'][0]
                self.display_amiibo_info(amiibo_data)
            else:
                self.response_label.setText("Amiibo not found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error fetching Amiibo data: {str(e)}")

    def display_amiibo_info(self, amiibo_data):
        name = amiibo_data.get('name', 'N/A')
        series = amiibo_data.get('amiiboSeries', 'N/A')
        release_date = amiibo_data.get('release', 'N/A')

        info_text = f"<b>Name:</b> {name}<br>" \
                    f"<b>Series:</b> {series}<br>" \
                    f"<b>Release Date:</b> {release_date}"

        self.response_label.setText(info_text)


def main():
    app = QApplication(sys.argv)
    amiibo_app = AmiiboApp()
    amiibo_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
