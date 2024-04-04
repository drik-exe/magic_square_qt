from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii




if __name__ == '__main__':
    keyPair = RSA.generate(2048)

    publicKey = keyPair.publickey()
    print(keyPair.p)
    print(f"Public key:  (n={hex(publicKey.n)}, e={hex(publicKey.e)})")
    privateKey = keyPair
    print(f"Private key: (n={hex(privateKey.n)}, d={hex(privateKey.d)})")

    msg = b'A message for encryption'
    encryptor = PKCS1_OAEP.new(publicKey)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", encrypted)

    decryptor = PKCS1_OAEP.new(privateKey)
    decrypted = decryptor.decrypt(encrypted)
    print('Decrypted:', decrypted)