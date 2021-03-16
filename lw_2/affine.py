from lw_1.euclidean_gcd import euclidean_gcd as egcd


class Affine:
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

        _, self.inv_a, _ = egcd(self.a, self.m)

    def encode(self, message: str):
        return ''.join([chr((self.a * ord(i) + self.b) % self.m) for i in message])

    def decode(self, message: str):
        return ''.join([chr((self.inv_a * (ord(i) - self.b)) % self.m) for i in message])


if __name__ == '__main__':
    a = Affine(3, 4, 1024)
    print(a.decode(a.encode('abc')))
