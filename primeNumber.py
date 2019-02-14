"""
2부터 N까지의 모든 소수의 합을 구하세요.
N이 7이라면 {2,3,5,7} = 17을 출력 하시면 됩니다.
N의 범위는 2이상 10,000,000이하 입니다.
효율성 테스트의 모든 시간 제한은 1초입니다.

https://programmers.co.kr/learn/courses/30/lessons/14406
"""


def is_prime_num(num):
    """
    소수인지 판별하는 함수
    :param n: 판별할 수
    :return: True or False
    """
    if n < 3:
        return True

    for j in range(2, num):
        remainder = num % j
        if remainder == 0 and j != num:
            return False
    return True


if __name__ == "__main__":
    print("N을 입력하시면 2부터 N 까지의 모든 소수의 합을 구합니다.")
    # n 의 값
    n = None
    while n is None:
        print("N의 값을 입력하세요 (N >= 2 and 1,000,000 >= N) : ", end="")
        n = int(input())
        if n <= 2 or n > 1000000:
            n = None
            print("N의 값이 범위를 초과하였습니다.")

    prime_num = []
    for i in range(2, n+1):
        res = is_prime_num(i)
        # print(i, res)
        if res is True:
            prime_num.append(i)
    # print(prime_num)
    print(sum(prime_num))
