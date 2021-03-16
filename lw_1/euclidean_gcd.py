def euclidean_gcd(a: int, b: int) -> (int, int, int):
    """
    :return: int: greatest common divisor, int: modular inversion (a^-1)
    """
    if not a:
        return b, 0, 1

    b_div_a, b_mod_a = divmod(b, a)
    g, x, y = euclidean_gcd(b_mod_a, a)
    return g, y - b_div_a * x, x


if __name__ == '__main__':
    print(euclidean_gcd(3, 26))
