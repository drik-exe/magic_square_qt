import numpy as np

def generate_utson_key(key):
    key = key.replace(" ", "").upper()
    key1 = key[:len(key)//2]
    key2 = key[len(key)//2:]
    key1 += "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-"
    key2 += "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-"
    new_key1 = ''
    new_key2 = ''
    for i in key1:
        if i not in new_key1:
            new_key1 += i
    new_key1 = np.array(list(new_key1))
    new_key1 = new_key1.reshape(5, 6)

    for i in key2:
        if i not in new_key2:
            new_key2 += i
    new_key2 = np.array(list(new_key2))
    new_key2 = new_key2.reshape(5, 6)

    return new_key1, new_key2



def find_position(key_matrix, letter):
    for i in range(5):
        for j in range(6):
            if key_matrix[i][j] == letter:
                return i, j

def encrypt_utson(plain_text, key):
    plain_text = plain_text.replace(" ", "_").upper()
    key_matrix1, key_matrix2 = generate_utson_key(key)

    cipher_text = ""
    i = 0

    while i < len(plain_text):
        letter1 = plain_text[i]
        letter2 = plain_text[i + 1] if i + 1 < len(plain_text) else "X"
        i += 2
        row1, col1 = find_position(key_matrix1, letter1)
        row2, col2 = find_position(key_matrix2, letter2)
        if row1 == row2:
            cipher_text += key_matrix1[row2][col2]
            cipher_text += key_matrix2[row1][col1]
        else:
            cipher_text += key_matrix1[row1][col2]
            cipher_text += key_matrix2[row2][col1]
    return cipher_text, key_matrix1, key_matrix2


def decrypt_utson(plain_text, key):
    plain_text = plain_text.replace(" ", "_").upper()
    key_matrix1, key_matrix2 = generate_utson_key(key)

    cipher_text = ""
    i = 0

    while i < len(plain_text):
        letter1 = plain_text[i]
        letter2 = plain_text[i + 1] if i + 1 < len(plain_text) else "X"
        i += 2
        row1, col1 = find_position(key_matrix1, letter1)
        row2, col2 = find_position(key_matrix2, letter2)
        if row1 == row2:
            cipher_text += key_matrix1[row2][col2]
            cipher_text += key_matrix2[row1][col1]
        else:
            cipher_text += key_matrix1[row1][col2]
            cipher_text += key_matrix2[row2][col1]
    return cipher_text

if __name__ == "__main__":
    key = "YONUFAXDYA"
    plain_text = "how are you my boy"
    cipher_text = encrypt_utson(plain_text, key)
    decrypted_text = decrypt_utson(cipher_text[0], key)

    print("Cipher Text:", cipher_text[0])
    print("Decrypted Text:", decrypted_text)  #GPS-OVD.FKN.LB_MUP