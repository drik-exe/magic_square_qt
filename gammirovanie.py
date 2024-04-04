import sys
import qdarkstyle
import time
import threading
from PyQt5.QtWidgets import *
from layouts.gamma import Ui_MainWindow
from encryption.gammirovanie import *

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setupUi(self)

        self.encrypt.clicked.connect(self.encrypt_button)
        self.decrypt.clicked.connect(self.decrypt_button)
        self.load.clicked.connect(self.load_file)
        self.save.clicked.connect(self.save_file)


    def load_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Files (*.txt)')

        if file_dialog.exec_():
            file = file_dialog.selectedFiles()[0]

            with open(file, "r") as f:
                data = f.read()

            self.mes.setPlainText(data)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            with open(file_name, "w") as f:
                f.write(self.dec_mes.toPlainText())


    def set_gamma(self):
        gamma = generate_gamma(len(self.mes.toPlainText()))
        self.gamma.setPlainText(' '.join(map(str, gamma)))

    def schedule_function(self):
        while True:
            try:
                self.set_gamma()
            except Exception as e:
                print(e)
            time.sleep(0.5)


    def encrypt_button(self):
        try:
            message = self.mes.toPlainText().upper()
            gamma = list(map(int, self.gamma.toPlainText().split()))
            enc_mes = enc_gammirovanie(message, gamma)
            self.dec_mes.setPlainText(enc_mes[0])

            with open('gamma.txt', "w") as f:
                f.write(' '.join(map(str, gamma)))
        except Exception as e:
            print(e)


    def decrypt_button(self):
        message = self.mes.toPlainText().upper()
        # gamma = ''
        with open('gamma.txt', "r") as f:
            gamma = f.read()
            print(gamma)

        dec_mes = dec_gammirovanie(message, map(int, gamma.split()))
        self.dec_mes.setPlainText(dec_mes)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()
    thread = threading.Thread(target=window.schedule_function, daemon=True)
    thread.start()
    window.show()
    sys.exit(app.exec_())
