def get_prime_numbers(upper: int):
    simple = list(range(upper + 1))
    simple[1] = 0
    for i in simple:
        if i > 1:
            for j in range(i + i, len(simple), i):
                simple[j] = 0
    return [i for i in simple if i != 0]


if __name__ == '__main__':
    print(get_prime_numbers(10))
