TestArr = range(2, 101)

# массив нечетных чисел
OddIntNum = []
# массив простых чисел
SimpleNum = []

for i in range(len(TestArr)):
    if TestArr[i] == 2:
        OddIntNum.append(TestArr[i])
    else:
        if TestArr[i] % 2 != 0:
            OddIntNum.append(TestArr[i])


# функция проверки числа на простоту
def is_simple_number(n):
    flag = True

    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


# print(is_simple_number(5))

# сохранили флаги проверки на простоту во массиве простых чисел
for i in range(len(OddIntNum)):
    SimpleNum.append(is_simple_number(OddIntNum[i]))
    if SimpleNum[i]:
        print(OddIntNum[i])
