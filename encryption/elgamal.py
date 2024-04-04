import random

alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
            'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
            'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
            'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

reversed_alphabet = {value: key for key, value in alphabet.items()}

primes = [29, 103, 241, 401, 571, 739, 919, 457, 659]
roots = [2, 5, 7, 3, 3, 3, 7, 13, 2]

def encrypt_el_gamal(mes):
    some = random.randint(0, len(primes)-1)
    some2 = random.randint(0, len(primes)-1)
    p = primes[some]
    g = roots[some2]
    x = random.randint(2, p)
    y = g**x % p
    k = random.randint(2, p-1)
    shifr_text = []
    for i in range(len(mes)):
        a = g**k % p
        b = y**k*alphabet[mes[i].upper()] % p
        shifr_text.append((a, b))

    return shifr_text, p, x, g, y


def decrypt_el_gamal(shifr_text, p, x):
    word = ''
    for i in range(len(shifr_text)):
        a, b = shifr_text[i]
        word += reversed_alphabet[b * a**(p - 1 - x) % p]
    return word


def to_plaintext(lst):
    s = ''
    for i in lst:
        s += f'{i[0]} {i[1]} '
    return s


def to_lst(text):
    lst = []
    t_split = text.split(' ')[:-1]
    for i in range(0, len(t_split), 2):
        lst.append((int(t_split[i]), int(t_split[i+1])))
    return lst


if __name__ == '__main__':
    a = encrypt_el_gamal('hello')
    b = decrypt_el_gamal(a[0], a[1], a[2])
    print(a[0], a[1], a[2], b)
    tp = to_plaintext(a[0])
    print(to_lst(tp))


