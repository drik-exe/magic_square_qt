import sys
from PyQt5.QtWidgets import *
from layouts.backpack import Ui_MainWindow
from encryption.backpack import *
from tabulate import tabulate

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
                data = f.readlines()
            self.close_key.setPlainText(data[0][:-1])
            self.open_key.setPlainText(data[1][:-1])
            self.mes.setPlainText(data[2][:-1])
            self.n.setPlainText(data[3][:-1])
            self.n1.setPlainText(data[4][:-1])
            self.m.setPlainText(data[5])



    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            with open(file_name, "w") as f:
                f.write(self.close_key.toPlainText() + '\n')
                f.write(self.open_key.toPlainText() + '\n')
                f.write(self.mes.toPlainText()+ '\n')
                f.write(self.n.toPlainText()+ '\n')
                f.write(self.n1.toPlainText()+ '\n')
                f.write(self.m.toPlainText())



    def encrypt_button(self):
        message = self.mes.toPlainText()
        k_i = list(map(int, self.close_key.toPlainText().split()))
        if len(k_i) < 7:
            k_i = create_k_i(k_i[0])
        m = self.m.toPlainText()
        if len(m) < 1:
            m = create_m(k_i)
        else:
            m = int(m)
        n = int(self.n.toPlainText())

        enc_mes = encrypt(message, k_i, m, n)
        if isinstance(enc_mes, str):
            self.dec_mes.setPlainText(enc_mes)
        else:
            self.dec_mes.setPlainText(' '.join(map(str, enc_mes[0])))

            table = []
            for i in range(len(message)):
                row = []
                row.append(message[i])
                row.append(enc_mes[3][i])
                row.append('_'.join(map(str, enc_mes[2][i])))
                row.append(''.join(str(enc_mes[0][i])))
                table.append(row)

            table_str = "Символ    | bin code     | сумма весов                       | c_i шифрограмма\n"
            for row in table:
                table_str += f"{row[0]:<16} | {row[1]:<12} | {row[2]:<16} | {row[3]}\n"


            self.plainTextEdit_6.setPlainText(table_str)




    def decrypt_button(self):
        c_i = list(map(int, self.mes.toPlainText().split()))
        k_i = list(map(int, self.close_key.toPlainText().split()))
        m = int(self.m.toPlainText())
        n = self.n.toPlainText()
        n1 = self.n1.toPlainText()
        if len(n) < 1:
            n = create_n(m)
        else:
            n = int(n)
            if not is_n_correct(n, m):
                self.dec_mes.setPlainText('n is not working')
                return False

        if len(n1) < 1:
            n1 = find_n1(n, m)
            dec_mes = decrypt(c_i, k_i, m, n, n1)
        else:
            n1 = int(n1)
            if not is_n1_correct(n1, n, m):
                self.dec_mes.setPlainText('n1 is not working')
                return False
            dec_mes = decrypt(c_i, k_i, m, n, n1)


        self.dec_mes.setPlainText(dec_mes[0])

        table = ''

        for i in range(len(dec_mes[0])):
            table += str(dec_mes[1][i])
            table += ' ' + str(dec_mes[2][i])
            table += ' ' + '_'.join(map(str, dec_mes[3][i]))
            table += ' ' + dec_mes[4][i]
            table += '\n'
        self.plainTextEdit_6.setPlainText(table)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()

    window.show()
    sys.exit(app.exec_())