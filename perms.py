print("Введите строку")
s = input()
print("Введите длину перестановок")
l = 0
while True:
    x = input()
    if "." in s or "-" in s:
        print("Длина должна быть натуральной")
        continue
    try:
        l = int(x)
    except:
        print("Введите число кооректно")
        continue
    break
p = []
us = []
for i in range(len(s)):
    us.append(0)
kl = 1


def f(ln):
    global kl
    if ln == 0:
        print(f"{kl}: ", end="")
        for i in p:
            print(i, end="")
        print("")
        kl += 1
    else:
        for i in range(len(s)):
            if us[i] == 0:
                p.append(s[i])
                us[i] = 1
                f(ln - 1)
                us[i] = 0
                p.pop()


f(l)