from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QLineEdit

code = {
    "a": ".-",    "b": "-...",    "c": "-.-.",    "d": "-..",    "e": ".",    "f": "..-.",    "g": "--.",    "h": "....",    "i": "..",    "j": ".---",    "k": "-.-",    "l": ".-..",    "m": "--",    "n": "-.",    "o": "---",    "p": ".--.",    "q": "--.-",    "r": ".-.",    "s": "...",    "t": "-",    "u": "..-",    "v": "...-",    "w": ".--",    "x": "-..-",    "y": "-.--",    "z": "--.."}


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Азбука Морзе 2")
        self.setGeometry(300, 300, 330, 100)
        alphabet_buttons = dict()

        for i, key in enumerate(list(code.keys())):
            btn = QPushButton(key, self)
            btn.resize(20, 20)
            btn.move(10 + (i * 20) % 300, 10 + ((i * 20) // 300) * 20)
            btn.clicked.connect(self.add_code)
            alphabet_buttons[key] = btn
        self.result = QLineEdit(self)
        self.result.move(10, 50)
        self.result.resize(280, 20)
        self.alphabet_buttons = alphabet_buttons

    def add_code(self):
        self.result.setText(self.result.text() + code[self.sender().text()])
