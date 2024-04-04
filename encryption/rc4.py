def rc4_init(s, key):
    for i in range(256):
        s.append(i)
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]


def rc4_crypt(s, data):
    i = j = 0
    result = []
    for char in data:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        result.append(char ^ k)
    return bytes(result)


def rc4(key, data):
    s = []
    rc4_init(s, key)
    return rc4_crypt(s, data)



if __name__ == "__main__":
    key = b"key"
    data = b"Hello, World!"

    encrypted = rc4(key, data)
    print(f"Зашифрованные данные: {encrypted}")

    decrypted = rc4(key, encrypted)
    print(f"Расшифрованные данные: {decrypted}")

    # Зашифрованные
    # данные: b"C\tX\x81K\xa3[\x1d'9d\x1f7"
    # Расшифрованные
    # данные: b'Hello, World!'