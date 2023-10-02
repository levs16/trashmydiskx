from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QApplication


class Suffle(QWidget):
    def init(self):
        super().init()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 330)
        self.setWindowTitle('Перемешивание:')
        self.button = QPushButton('Загрузить строки', self)

        self.button.move(10, 10)
        self.text_field = QTextBrowser(self)

        self.text_field.move(10, 40)
        self.text_field.resize(280, 280)

        self.button.clicked.connect(self.load_strings)

    def load_strings(self):
        with open('lines.txt', encoding='utf-8') as f:
            text = f.read().strip().split('\n')
        self.text_field.setText(
            "\n".join(text[1::2]) + "\n" + "\n".join(text[::2]))
