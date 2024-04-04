import string

def generate_vigenere_matrix(key):
    alphabet = string.ascii_uppercase
    matrix = []
    for char in key:
        shifted_alphabet = char + alphabet[:alphabet.index(char)] + alphabet[alphabet.index(char)+1:]
        matrix.append(shifted_alphabet)
    return matrix

def vigenere_cipher(text, key):
    matrix = generate_vigenere_matrix(key)
    printed_matrix = matrix
    encrypted_text = ""
    for i, char in enumerate(text):
        row = i % len(key)
        col = string.ascii_uppercase.index(char)
        encrypted_text += matrix[row][col]
    return encrypted_text, printed_matrix

def vigenere_decipher(text, key):
    matrix = generate_vigenere_matrix(key)
    decrypted_text = ""
    for i, char in enumerate(text):
        row = i % len(key)
        col = matrix[row].index(char)
        decrypted_text += string.ascii_uppercase[col]
    return decrypted_text


def encrypt(text, vigenere_key):
    vigenere_ciphertext = vigenere_cipher(text, vigenere_key)
    return vigenere_ciphertext


def decrypt(ciphertext, vigenere_key):
    vigenere_plaintext = vigenere_decipher(ciphertext, vigenere_key)
    return vigenere_plaintext

plaintext = "HELLOWORD"
vigenere_key = "KEY"

if __name__ == '__main__':
    ciphertext = encrypt(plaintext, vigenere_key)
    print("Зашифрованный текст:", ciphertext[0])
    # print(ciphertext[1])

    decrypted_text = decrypt(ciphertext[0], vigenere_key)
    print("Расшифрованный текст:", decrypted_text)
# GDKLOVORC
