import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from layouts.el_gamal import Ui_MainWindow
from encryption.elgamal import *

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
            p, x, g, y = data.split()
            self.mes_2.setPlainText(p)
            self.mes_3.setPlainText(x)
            self.mes_4.setPlainText(g)
            self.mes_5.setPlainText(y)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            with open(file_name, "w") as f:
                f.write(self.dec_mes.toPlainText())



    def encrypt_button(self):
        message = self.mes.toPlainText()
        enc_mes = encrypt_el_gamal(message)
        self.dec_mes.setPlainText(to_plaintext(enc_mes[0]))
        with open('pxgy.txt', "w") as f:
            f.write(f'{enc_mes[1]} {enc_mes[2]} {enc_mes[3]} {enc_mes[4]}')

        with open('pgy.txt', 'w') as f:
            f.write(f'p = {enc_mes[1]} g = {enc_mes[3]} y = {enc_mes[4]}')

        with open('x.txt', 'w') as f:
            f.write(f'x = {enc_mes[2]}')



    def decrypt_button(self):
        message = self.mes.toPlainText()
        message = to_lst(message)
        p = int(self.mes_2.toPlainText())
        x = int(self.mes_3.toPlainText())
        dec_mes = decrypt_el_gamal(message, p, x)
        self.dec_mes.setPlainText(dec_mes)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()

    window.show()
    sys.exit(app.exec_())
