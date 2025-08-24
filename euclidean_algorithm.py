def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ext_euclid_back_substitution(a, b):
    '''r,s,t'''
    r = [a, b, a % b]
    q = [0, r[0] // r[1]]
    j = 2
    # flag = True
    while r[j] != 0:
        # q_j = r_{j-1} / r_j
        q.append(r[j - 1] // r[j])
        # r_{j+1} = r_{j-1} - q_j * r_j
        r.append(r[j - 1] % r[j])
        j += 1
    s = [1, 0]
    t = [0, 1]
    for j in range(2, len(r)-1):
        # s_j = s_{j-2} - q_{j-1} * s_{j-1}
        s.append(s[j - 2] - (q[j - 1] * s[j - 1]))
        # t_j = t_{j-2} - q_{j-1} * t_{j-1}
        t.append(t[j - 2] - (q[j - 1] * t[j - 1]))
    return r[-2], s[-1], t[-1]


def ext_euclid(a, b):
    '''return r,s,t (s*a+t*b=r)'''
    r_0, s_0, t_0 = a, 1, 0
    r_1, s_1, t_1 = b, 0, 1
    while r_1 != 0:
        q = r_0//r_1
        temp_1 = r_0%r_1
        temp_2 = s_0-q*s_1
        temp_3 = t_0-q*t_1
        r_0, s_0, t_0 = r_1, s_1, t_1
        r_1, s_1, t_1 = temp_1, temp_2, temp_3
    return r_0, s_0, t_0

def test():
    a, b = 252, 198
    # test
    d_0 = gcd(a, b)
    print('euclid: gcd(%d, %d)= %d' % (a, b, d_0))

    d_1, s_1, t_1 = ext_euclid_back_substitution(a, b)
    print('ext_euclid_back_substitution: ', end='')
    print(s_1, '*', a, '+', t_1, '*', b, '=', d_1)

    d_2, s_2, t_2 = ext_euclid(a, b)
    print('ext_euclid: ', end='')
    print(s_2, '*', a, '+', t_2, '*', b, '=', d_2)


def main():
    a = int(input('Input a:'))
    b = int(input('Input b:'))
    d, s, t = ext_euclid(a, b)
    print('%d * %d + %d * %d = %d' % (s, a, t, b, d))


if __name__ == '__main__':
    test()