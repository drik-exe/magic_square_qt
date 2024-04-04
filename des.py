import sys
from PyQt5.QtWidgets import *
from layouts.des import Ui_MainWindow
from encryption.des import *


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setupUi(self)

        self.encrypt.clicked.connect(self.encrypt_button)
        self.decrypt.clicked.connect(self.decrypt_button)
        self.encrypt_3.clicked.connect(self.load_file)
        self.save.clicked.connect(self.save_file)

        self.super_word = None

    def load_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Files (*.des)')

        if file_dialog.exec_():
            file1 = file_dialog.selectedFiles()[0]

            ciphertext_from_file = read_from_file(file1)

            self.super_word = ciphertext_from_file


    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            save_to_file(f'{file_name}.des', self.super_word)

    def encrypt_button(self):
        message = bytes(self.mes.toPlainText(), 'utf')
        key = bytes(self.open_key.toPlainText(), 'utf')

        message = pad(message)

        encrypted = des_encrypt(message, key)
        self.super_word = encrypted

        self.dec_mes.setPlainText(str(binascii.hexlify(encrypted))[2:-1])

    def decrypt_button(self):
        message = self.super_word
        key = bytes(self.open_key.toPlainText(), 'utf')

        decrypted = des_decrypt(message, key)

        self.dec_mes.setPlainText(str(decrypted)[2:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()

    window.show()
    sys.exit(app.exec_())
