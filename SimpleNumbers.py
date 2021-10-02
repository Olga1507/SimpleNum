TestArr = range(2, 1002)


# функция проверки числа на простоту
def is_simple_number(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


# вывод простых чисел
for i in range(len(TestArr)):
    if is_simple_number(TestArr[i]):
        print(TestArr[i])
