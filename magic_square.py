import sys

import qdarkstyle
from PyQt5.QtWidgets import *
from layouts.magic_square_layout import Ui_MainWindow
from encryption.magic_square import *
import numpy as np


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.setMinimumWidth(700)
        self.setMinimumHeight(500)
        self.setupUi(self)

        self.enc_btn.clicked.connect(self.encrypt_button_clicked)
        self.dec_btn.clicked.connect(self.decrypt_button_clicked)
        self.opne_btn.clicked.connect(self.load_file)
        self.save_btn.clicked.connect(self.save_file)

    def load_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Files (*.txt)')

        if file_dialog.exec_():
            file = file_dialog.selectedFiles()[0]

            with open(file, "r") as f:
                data = f.read()

            self.message_enc.setPlainText(data)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            with open(file_name, "w") as f:
                f.write(self.dec_mes.toPlainText())

    def encrypt_button_clicked(self):
        message = self.message_enc.toPlainText()

        size_of_matrix = int(np.ceil(np.sqrt(len(message))))

        if size_of_matrix > 3:
            self.enc_mes.setPlainText("Message is too long to encrypt")
        else:
            magic_matrix = generate_magic_squares()
            encypto_matrix = encypt(message, magic_matrix)

            s = ''.join(j for i in encypto_matrix for j in i)

            s_magic_matrix = ''
            for i in magic_matrix:
                for j in i:
                    s_magic_matrix += str(j)
                s_magic_matrix += '\n'
            self.enc_mes.setPlainText(s)

            self.matrix1.setPlainText(s_magic_matrix)

            s_magic_matrix_string = f'{s[0:3]}\n{s[3:6]}\n{s[6:9]}'

            self.matrix2.setPlainText(s_magic_matrix_string)

    def decrypt_button_clicked(self):
        key1 = self.key1.toPlainText()
        message = self.message_dec.toPlainText()
        if key1[-1] == '\n':
            key1 = key1[:-1]

        pre_magic_matrix = key1.split('\n')

        magic_matrix = [[int(j) for j in i] for i in pre_magic_matrix]

        pre_enrypto_matrix = [message[i:i + 3] for i in range(0, len(message), 3)]
        encrypto_matrix = [[j for j in i] for i in pre_enrypto_matrix]

        dec_crypto_string = decrypt(magic_matrix, encrypto_matrix)
        self.dec_mes.setPlainText(dec_crypto_string)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()
    window.show()
    sys.exit(app.exec_())