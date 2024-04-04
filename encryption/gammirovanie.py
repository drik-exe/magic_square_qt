import random

mapping = {
    1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ж', 8: 'З', 9: 'И', 10: 'К',
    11: 'Л', 12: 'М', 13: 'Н', 14: 'О', 15: 'П', 16: 'Р', 17: 'С', 18: 'Т', 19: 'У',
    20: 'Ф', 21: 'Х', 22: 'Ц', 23: 'Ч', 24: 'Ш', 25: 'Щ', 26: 'Ъ', 27: 'Ы', 28: 'Ь',
    29: 'Э', 30: 'Ю', 31: 'Я', 32: '0', 33: '1', 34: '2', 35: '3', 36: '4', 37: '5',
    38: '6', 39: '7', 40: '8', 41: '9'
}

reversed_mapping = {value: key for key, value in mapping.items()}

def get_sequance(mes: str):
    numbers_sequance = []
    for i in mes:
        numbers_sequance.append(reversed_mapping[i])
    return numbers_sequance


def generate_gamma(length):
    x = []
    while len(x) < length:
        random_number = random.randint(1, 41)
        if random_number not in x:
            x.append(random_number)
    return x


def enc_gammirovanie(mes, gamma):
    z = get_sequance(mes)
    x = gamma
    y = [(i + j) % len(mapping) for i, j in zip(z, x)]

    enc_mes = ''.join([mapping[i] for i in y])
    return enc_mes, x


def dec_gammirovanie(mes, x):
    enc_mes = [reversed_mapping[i] for i in mes]
    z = [(i + len(mapping) - j) % len(mapping) for i, j in zip(enc_mes, x)]
    dec_mes = ''.join([mapping[i] for i in z])
    return dec_mes


if __name__ == '__main__':
    mes = input().upper()
    x = generate_gamma(len(mes))
    a = enc_gammirovanie(mes, x)
    print(a[0], a[1])
    b = dec_gammirovanie(a[0], a[1])
    print(b)