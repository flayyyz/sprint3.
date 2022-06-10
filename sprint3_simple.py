if __name__ == '__main__':

    max_k = 5
    max_n = 40
    verification_string = 'введите 2 положительных целых числа n≤40 и k≤5 через пробел\n' \
                          'Пример входных данных:\n' \
                          '5 3'

    while True:
        input_string = input()
        try:
            n, k = map(int, input_string.split(' '))
            if n <= 0 or k <= 0 or n > max_n or k > max_k:
                raise ValueError
            break
        except ValueError:
            print(verification_string)

    s0 = 1
    s1 = 0

    for i in range(n - 1):
        temp = s0 + s1
        s0 = k * s1
        s1 = temp

    print('ответ:', s1 + s0)
