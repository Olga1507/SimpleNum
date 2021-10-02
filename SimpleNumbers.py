import time

start_time = time.time()

ResultArr = []


# функция проверки числа на простоту
def is_simple_number(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


# вывод простых чисел в массив
for i in range(2, 1002):
    if is_simple_number(i):
        ResultArr.append(i)
        # print(i)

print("--- %s seconds ---" % (time.time() - start_time))
