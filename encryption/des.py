from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


def save_to_file(file_name, data):
    with open(file_name, 'wb') as f:
        f.write(data)


def read_from_file(file_name):
    with open(file_name, 'rb') as f:
        return f.read()


def des_encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(pad(plaintext))


def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(ciphertext).rstrip(b' ')


if __name__ == '__main__':
    # key = get_random_bytes(8)
    key = b'12345678'
    print(key)
    t = 'This is a secret message.'
    plaintext = bytes(t, 'utf')
    plaintext = pad(plaintext)
    ciphertext = des_encrypt(plaintext, key)


    save_to_file('../ciphertext.des', ciphertext)
    save_to_file('../key.des', key)

    print(f'Ciphertext (hex): {binascii.hexlify(ciphertext)}')

    ciphertext_from_file = read_from_file('../ciphertext.des')
    key_from_file = read_from_file('../key.des')

    decrypted = des_decrypt(ciphertext_from_file, key_from_file)

    print(f'Decrypted text: {decrypted}')
