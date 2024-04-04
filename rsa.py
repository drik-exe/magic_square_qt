import sys
import ast
from Crypto.PublicKey.RSA import RsaKey
from PyQt5.QtWidgets import *
from layouts.rsa import Ui_MainWindow
from encryption.rsa import *


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(600)
        self.setupUi(self)

        self.encrypt.clicked.connect(self.encrypt_button)
        self.decrypt.clicked.connect(self.decrypt_button)
        self.open.clicked.connect(self.load_file)
        self.save.clicked.connect(self.save_file)
        self.generate.clicked.connect(self.generate_keys)

    def load_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Files (*.txt)')

        if file_dialog.exec_():
            file = file_dialog.selectedFiles()[0]

            with open(file, 'r') as f:
                self.mes.setPlainText(f.read())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.dec_mes.toPlainText())

    def generate_keys(self):
        keyPair = RSA.generate(2048)

        publicKey = keyPair.publickey()

        privateKey = keyPair

        self.open_key.setPlainText(f"{publicKey.n} {publicKey.e}")
        self.closed_key.setPlainText(f"{privateKey.p} {privateKey.q} {privateKey.d} {privateKey.u}")

    def encrypt_button(self):
        message = bytes(self.mes.toPlainText(), 'utf')
        open_key = self.open_key.toPlainText().split()
        open_key = {'n': int(open_key[0]), 'e': int(open_key[1])}


        keyPair = RsaKey(n=open_key['n'], e=open_key['e'])
        publicKey = keyPair.publickey()

        encryptor = PKCS1_OAEP.new(publicKey)
        encrypted = encryptor.encrypt(message)
        print(str(encrypted))
        self.dec_mes.setPlainText(str(encrypted))

    def decrypt_button(self):
        message = self.mes.toPlainText()
        message = ast.literal_eval(message)
        print(message)
        open_key = self.open_key.toPlainText().split()
        open_key = {'n': int(open_key[0]), 'e': int(open_key[1])}
        closed_key = self.closed_key.toPlainText().split()
        closed_key = {'p': int(closed_key[0]), 'q': int(closed_key[1]), 'd': int(closed_key[2]),
                      'u': int(closed_key[3])}

        keyPair = RsaKey(n=open_key['n'], e=open_key['e'], p=closed_key['p'], d=closed_key['d'], u=closed_key['u'],
                         q=closed_key['q'])
        privateKey = keyPair

        decryptor = PKCS1_OAEP.new(privateKey)
        decrypted = decryptor.decrypt(message)

        self.dec_mes.setPlainText(str(decrypted)[2:-1])




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()

    window.show()
    sys.exit(app.exec_())
