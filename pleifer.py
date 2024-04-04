import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from layouts.layout import Ui_MainWindow
from encryption.viginer import *
from encryption.pleifer import *

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

        self.vig_dec_key = ''
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
        v_key = self.vigener_key.toPlainText().upper()
        v_mes = self.vigener_mes.toPlainText().upper()
        message = self.text.toPlainText().upper()
        enc_mes = encrypt(v_mes, v_key)
        self.vig_dec_key = enc_mes[0]
        s = '\n'.join(enc_mes[1])
        key = ''
        for i in enc_mes[1]:
            key += str(i[0])

        self.matrix_vigenera.setPlainText(f'{s}\nkey: {key}')


        enc_mes = encrypt_playfair(message, enc_mes[0])
        self.dec_mes.setPlainText(enc_mes[0])
        a = [list(i) for i in enc_mes[1]]
        s = ''
        for i in a:
            for j in i:
                s += j
            s += '\n'

        self.matrix_pleifera.setPlainText(s)

    def decrypt_button(self):
        v_key = self.vigener_key.toPlainText().upper()
        # v_mes = self.vigener_mes.toPlainText().upper()

        message = self.text.toPlainText().upper()
        dec_mes = decrypt_playfair(message, self.vig_dec_key)
        self.dec_mes.setPlainText(dec_mes)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()
    window.show()
    sys.exit(app.exec_())
