"""Case-study #7 Генерация предложений
Разработчики:
Bayanova A., Shmatov D.

"""
import random

first = []
last = []

text = input('Введите имя файла: ')
f_in = open(text, 'r')
pov = int(input('Количество генерируемых предложений: '))
for line in f_in:
    line = line.replace("&", "")
    line = line.replace("^", "")
    line = line.replace("%", "")
    line = line.replace("$", "")
    line = line.replace("#", "")
    line = line.replace("*", "")
    line = line.replace("-", "")
    line = line.replace("=", "")
    line = line.replace("+", "")
    line = line.replace("@", "")
    line = line.replace(")", "")
    line = line.replace("(", "")
    line = line.replace("/", "")
    line = line.replace(":", "")
    line = line.replace(";", "")

    line = line.replace(" .", ".")
    line = line.replace(" ,", ",")
    line = line.replace(" !", "!")
    line = line.replace(" ?", "?")
    line = line.replace(".", ". ")
    line = line.replace(",", ", ")
    line = line.replace("!", "! ")
    line = line.replace("?", "? ")
    line = line.replace("  ", " ")
    print(f_in)


    d = {}
    e = []
    s = list(f_in.split())  # за место line было f_in
    for j in range(1, len(s)):
        if not s[j-1] in d:
            d[s[j-1]] = []
        d[s[j - 1]].append(s[j])
        if  len(d[s[j - 1]]) > 1:
            if s[j-1] not in e:
                e.append(s[j - 1])

    for i in range(len(s)):
        if s[i][0] == s[i][0].upper():
            if s[i][-1] not in "!?.":
                first.append(s[i])
        if s[i][-1] in ".!?":
            last.append(s[i])

    print(d)  # выводит словарь

print(first)  # выводит список первых слов

print(last)  # выводит список последних слов

print(e)  # выводит список слов не с одним значением ключа


for i in range(pov):
    nachalo = random.choice(first)
    slovo = random.choice(d.get(nachalo))
    coun = random.choice(range(5, 21))
    print(nachalo, end = " ")
    for j in range(coun):
        slovo = random.choice(d.get(slovo))
        if slovo[-1] != ".":
            print(slovo, end = " ")
        if j == (coun - 1):
            while slovo[-1] != ".":
                slovo = random.choice(d.get(slovo))
            print(slovo, end = " ")
