from random import randrange

from lw_1.euclidean_gcd import euclidean_gcd as egcd
from lw_1.linear_comparison import linear_comparison


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


class Rsa:
    def __init__(self, p, q):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')

        self.p = p
        self.q = q
        self.public_key = None
        self.private_key = None
        self.init_key_pair()

    def init_key_pair(self):
        n = self.p * self.q

        m = (self.p - 1) * (self.q - 1)

        g, pub_k = -1, -1
        while g != 1 or not (1 < pub_k < m):
            pub_k = randrange(1, m)
            g, d, _ = egcd(pub_k, m)

        self.public_key = pub_k, n
        self.private_key = linear_comparison(pub_k, 1, m), n

    @staticmethod
    def processing(message, key):
        power, n = key
        return ''.join([chr((int(ord(i)) ** int(power)) % n) for i in message])

    def encode(self, message):
        return self.processing(message, self.public_key)

    def decode(self, message):
        return self.processing(message, self.private_key)


if __name__ == '__main__':
    rsa = Rsa(23, 37)
    print(rsa.encode('asd'))
    print(rsa.decode(rsa.encode('asd')))
