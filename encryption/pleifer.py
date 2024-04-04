import numpy as np


def create_to_str(key):
    a = [list(i) for i in key]
    s = ''
    for i in a:
        for j in i:
            s += j
        s += '\n'
    return s

def generate_playfair_key(key):
    key = key.replace(" ", "").upper()
    key += "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-"
    new_key = ''
    for i in key:
        if i not in new_key:
            new_key += i
    new_key = np.array(list(new_key))
    new_key = new_key.reshape(5, 6)
    return new_key


def find_position(key_matrix, letter):
    for i in range(5):
        for j in range(6):
            if key_matrix[i][j] == letter:
                return i, j

def encrypt_playfair(plain_text, key):
    plain_text = plain_text.replace(" ", "_").upper()
    key_matrix = generate_playfair_key(key)
    cipher_text = ""
    i = 0
    while i < len(plain_text):
        letter1 = plain_text[i]
        letter2 = plain_text[i + 1] if i + 1 < len(plain_text) else "X"
        i += 2
        row1, col1 = find_position(key_matrix, letter1)
        row2, col2 = find_position(key_matrix, letter2)
        if row1 == row2:
            cipher_text += key_matrix[row1][(col1 + 1) % 6]
            cipher_text += key_matrix[row2][(col2 + 1) % 6]
        elif col1 == col2:
            cipher_text += key_matrix[(row1 + 1) % 5][col1]
            cipher_text += key_matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += key_matrix[row1][col2]
            cipher_text += key_matrix[row2][col1]
    return cipher_text, key_matrix

def decrypt_playfair(cipher_text, key):
    cipher_text = cipher_text.replace(" ", "_").upper()
    key_matrix = generate_playfair_key(key)
    plain_text = ""
    i = 0
    while i < len(cipher_text):
        letter1 = cipher_text[i]
        letter2 = cipher_text[i + 1]
        i += 2
        row1, col1 = find_position(key_matrix, letter1)
        row2, col2 = find_position(key_matrix, letter2)
        if row1 == row2:
            plain_text += key_matrix[row1][(col1 - 1) % 6]
            plain_text += key_matrix[row2][(col2 - 1) % 6]
        elif col1 == col2:
            plain_text += key_matrix[(row1 - 1) % 5][col1]
            plain_text += key_matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += key_matrix[row1][col2]
            plain_text += key_matrix[row2][col1]
    return plain_text

if __name__ == '__main__':
    key = "key"
    plain_text = "anotherkey"
    cipher_text = encrypt_playfair(plain_text, key)
    decrypted_text = decrypt_playfair(cipher_text[0], key)

    print("Cipher Text:", cipher_text[0])
    print("Decrypted Text:", decrypted_text) #YONUFAXDYA