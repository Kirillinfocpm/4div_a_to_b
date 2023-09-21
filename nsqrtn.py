import time

print('Решение за O(n*sqrt(n))')
print(
    "Введите 2 натуральных числа числа на двух разных строках - границы отрезка (первое число меньше или равно второму)"
)
t = 1
while t == 1:
    a = input()
    if " " in a:
        print("Введите числа корректно на разных строках")
        continue
    b = input()
    if '-' in a or '-' in b or '.' in a or '.' in b:
        print("Числа должны быть натуральными")
        continue
    l = 0
    r = 0
    try:
        l = int(a)
    except:
        print("Введите числа (если что, они состоят из цифр)")
        continue
    try:
        r = int(b)
    except:
        print("Введите числа (если что, они состоят из цифр)")
        continue
    if l > r:
        print("Первое число должно быть меньше или равно второму")
        continue
    if l == 0:
        print("Числа должны быть натуральными")
        continue
    a = l
    b = r
    break
print(
    "Введите число 0 или 1 (0, если не выводить все числа и их делители, а вывести только количество чисел, 1, если вывести всё (очевидно, что 0 будет работать сильно быстрее)). Этот флаг нужен для оценки, насколько это решение быстрее решения за O(n*sqrt(n))"
)
fl = 0
t = 1
c = []
while t == 1:
    f = input()
    if f != "0" and f != "1":
        print("Введите 0 или 1")
        continue
    fl = int(f)
    break
kl=0
tm0 = time.perf_counter()
for i in range(a, b + 1):
    ar = []
    j = 1
    if i > 4:
        while j * j <= i and len(ar) < 5:
            if i % j == 0:
                ar.append(j)
                if j * j != i:
                    ar.append(i // j)
            j += 1
    if len(ar) == 4:
        ar.sort()
        kl += 1
        if fl==1:
            c.append([i,i,ar[2],ar[1],ar[0]])
if fl == 1:
    c.sort()
    for ar in c:
        print(f"{ar[0]}: ({ar[1]}, {ar[2]}, {ar[3]}, {ar[4]})")
print(f"Всего {kl} чисел")
tm1 = time.perf_counter()
print(f'{tm1 - tm0} секунд')