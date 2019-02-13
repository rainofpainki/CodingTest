from fractions import gcd


def gcdlcm(a, b):
    """
    fractions 모듈을 이용한 방법
    :param a:
    :param b:
    :return:
    """
    gcd_value = gcd(a, b)
    lcm_value = int(a*b/gcd_value)
    return [gcd_value, lcm_value]


def gcdlcm2(a, b):
    """
    직접 계산하는 방법
    :param a:
    :param b:
    :return:
    """
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return [c, int(a*b/c)]


if __name__ == "__main__":
    print(gcdlcm(3, 12))
    print(gcdlcm2(3, 12))


# ref : https://wayhome25.github.io/algorithm/2017/03/08/gcdlcm/
