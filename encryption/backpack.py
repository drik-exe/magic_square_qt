def message_to_bianry(message: str) -> list:
    binary_message = ""
    for char in message:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_message += binary_char[1:] + ' '
    return binary_message.split()

def binary_to_message(message: list) -> str:
    decrypted_message = ""
    binary_message = ""
    for i in message:
        binary_message += '0' + str(i)
    for i in range(0, len(binary_message), 8):
        binary_char = binary_message[i:i+8]
        char = chr(int(binary_char, 2))
        decrypted_message += char
    return decrypted_message


def is_closed_key(k_i: list) -> bool:
    for i in range(1, len(k_i)):
        if k_i[i-1] * 2 > k_i[i]:
            return False
    return True

def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def is_n_correct(n: int, m: int) -> bool:
    if is_prime(n) and m % n != 0:
        return True
    else:
        return False

def is_n1_correct(n1, n, m):
    if (n * n1) % m == 1:
        return True
    else:
        return False

def is_m_correct(m: int, k_i: list) -> bool:
    if sum(k_i) > m:
        return False
    return True

def create_k_i(n: int = None):
    if n == None:
        n = 2
    k_i = [n]
    for i in range(1, 7):
        m = k_i[i-1]
        k_i.append(m * 2)
    return k_i

def create_m(k_i: list):
    sum = 0
    for i in k_i:
        sum += i
    return sum + 1

def encrypt(message: str, k_i: list, m: int, n: int):
    if not is_closed_key(k_i):
        return 'k_i is not working'

    if not is_m_correct(m, k_i):
        return 'm is not working'

    x_i = []
    for i in k_i:
        x_i.append((i * n) % m)

    bin_code = message_to_bianry(message)
    c_i = []
    sum_weights = []

    for i in bin_code:
        sum = 0
        weights = []
        for j in range(len(x_i)):
            if i[j] == '1':
                sum += x_i[j]
                weights.append(x_i[j])
            else:
                weights.append(' ')
        sum_weights.append(weights)
        c_i.append(sum)


    return c_i, k_i, sum_weights, bin_code


def create_n(m):
    simple_number = [31, 37, 41, 43, 47, 53, 59]
    for i in simple_number:
        if m % i != 0:
            return i
def find_n1(n, m):
    i = 0
    n1 = 0
    while True:
        i += 1
        if (n * i) % m == 1:
            n1 = i
            break
    return n1

def decrypt(c_i: list, k_i: list, m: int, n: int, n_1:int = None):
    if n_1 == None:
        n1 = find_n1(n, m)
    else:
        n1 = n_1
    a_i = []

    for i in c_i:
        a_i.append((i * n1) % m)

    sum_weights = []

    for i in a_i:
        sum = 0
        weights = []
        for j in k_i[::-1]:
            if sum + j <= i:
                sum += j
                weights.append(j)
            else:
                weights.append(' ')
        sum_weights.append(weights[::-1])


    bin_code = []
    for i in sum_weights:
        bin = ''
        for j in i:
            if j == ' ':
                bin += '0'
            else:
                bin += '1'
        bin_code.append(bin)

    dec_message = binary_to_message(bin_code)

    return dec_message, c_i, a_i, sum_weights, bin_code






if __name__ == '__main__':
    s = encrypt('abc', [2, 4, 8, 16, 32, 64, 128], 420, 31)
    d = decrypt(s[0], s[1], 420, 31)
    print(d[1], d[2], d[3], d[4])
    print(create_k_i(2))







