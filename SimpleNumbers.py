import time

start_time = time.time()


# функция проверки числа на простоту
def is_simple_number(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


# вывод простых чисел
for i in range(2, 100000):
    if is_simple_number(i):
        print(i)

print("--- %s seconds ---" % (time.time() - start_time))
