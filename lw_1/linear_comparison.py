def linear_comparison(a, b, m):
    a_s, b_s, m_s = a, b, m

    q = []

    while a != 0:
        tmp_a = m % a
        q.append((m - tmp_a) / a)
        m = a
        a = tmp_a

    n = len(q) - 1
    p = [1, q[0]]
    for i in q[1:n]:
        p.append(i * p[len(p) - 1] + p[len(p) - 2])

    return (((-1) ** n) * p[n] * b_s % m_s) % m_s


if __name__ == '__main__':
    print(linear_comparison(12, 8, 67))
