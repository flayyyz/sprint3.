def get_int_number(notification, verification, max_value):
    while True:
        try:
            value = int(input(notification))
            if value <= 0 or value > max_value:
                raise ValueError
            return value

        except ValueError:
            print(verification % max_value)


def calculate(n, k):
    s0 = 1
    s1 = 0

    for i in range(n - 1):
        temp = s0 + s1
        s0 = k * s1
        s1 = temp

    return s0 + s1


if __name__ == '__main__':
    verification_string = 'введите целое положительное число меньше или равное %d\n'
    notification_string = {'n': 'введите n: ', 'k': 'введите k: '}
    limit = {'n': 40, 'k': 5}

    n = get_int_number(notification_string['n'], verification_string, limit['n'])
    k = get_int_number(notification_string['k'], verification_string, limit['k'])

    answer = calculate(n, k)
    print('ответ:', answer)
