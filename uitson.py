import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from layouts.layout import Ui_MainWindow
from encryption.pleifer import *
from encryption.uitson import *

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

        self.plef_dec_key = ''
    def load_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Files (*.txt)')

        if file_dialog.exec_():
            file = file_dialog.selectedFiles()[0]

            with open(file, "r") as f:
                data = f.read()

            self.text.setPlainText(data)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            with open(file_name, "w") as f:
                f.write(self.dec_mes.toPlainText())

    def encrypt_button(self):
        p_key = self.pleifer_key.toPlainText().upper()
        p_mes = self.pleifer_mes.toPlainText().upper()
        message = self.mes.toPlainText().upper()
        enc_mes = encrypt_playfair(p_mes, p_key)
        self.plef_dec_key = enc_mes[0]

        self.matrix_pleifera.setPlainText(create_to_str(enc_mes[1]))

        enc_mes = encrypt_utson(message, enc_mes[0])
        self.dec_mes.setPlainText(enc_mes[0])
        self.matrix_vigenera_3.setPlainText(create_to_str(enc_mes[1]))
        self.matrix_uitson1.setPlainText(create_to_str(enc_mes[2]))

    def decrypt_button(self):
        message = self.mes.toPlainText().upper()
        print(message, self.plef_dec_key)
        dec_mes = decrypt_utson(message, self.plef_dec_key)
        self.dec_mes.setPlainText(dec_mes)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()
    window.show()
    sys.exit(app.exec_())
