import time

print("Решение за O(n*log(log(n)))")
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
tm0 = time.perf_counter()
c = []
pr = []
for j in range(0, r // 2 + 5):
    pr.append(False)
prm = []
for i in range(2, r // 2 + 5):
    if pr[i] == False:
        prm.append(i)
        for j in range(i * i, r // 2 + 5, i):
            pr[j] = True
n = len(prm)
kl = 0
l = 1
r = 0
while prm[0] * prm[l] < a:
    l += 1
while r + 1 < n and prm[0] * prm[r + 1] <= b:
    r += 1
for i in range(n - 1):
    if prm[i] * prm[i + 1] > b:
        break
    if l <= i:
        l = i + 1
    while l > i + 1 and prm[i] * prm[l - 1] >= a:
        l -= 1
    while prm[i] * prm[r] > b:
        r -= 1
    kl += r - l + 1
    if fl == 1:
        for j in range(l, r + 1):
            c.append([prm[i] * prm[j], prm[i] * prm[j], prm[j], prm[i], 1])
l = -1
r = n
while l + 1 < r:
    md = (l + r) // 2
    if prm[md] ** 3 < a:
        l = md
    else:
        r = md
smin = r
l = -1
r = n
while l + 1 < r:
    md = (l + r) // 2
    if prm[md] ** 3 > b:
        r = md
    else:
        l = md
kl += l - smin + 1
if fl == 1:
    for i in range(smin, l + 1):
        c.append([prm[i] ** 3, prm[i] ** 3, prm[i] ** 2, prm[i], 1])
if fl == 1:
    c.sort()
    for ar in c:
        print(f"{ar[0]}: ({ar[1]}, {ar[2]}, {ar[3]}, {ar[4]})")
print(f"Всего {kl} чисел")
tm1 = time.perf_counter()
print(f'{tm1 - tm0} секунд')
