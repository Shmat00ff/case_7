"""Case-study #7 Генерация предложений
Разработчики:
Bayanova A. 60%, Shmatov D. 70%

"""
import random

first = []
last = []
q = ""
text = input('Введите имя файла: ')
f_in = open(text, 'r')
pov = int(input('Количество генерируемых предложений: '))
for line in f_in:
    q = q + " " + line

q = q.replace("&", "")
q = q.replace("^", "")
q = q.replace("%", "")
q = q.replace("$", "")
q = q.replace("#", "")
q = q.replace("*", "")
q = q.replace("-", "")
q = q.replace("=", "")
q = q.replace("+", "")
q = q.replace("@", "")
q = q.replace(")", "")
q = q.replace("(", "")
q = q.replace("/", "")
q = q.replace("—", "")
q = q.replace("...", ".")
q = q.replace(":", "")
q = q.replace(";", "")
q = q.replace(" .", ".")
q = q.replace(" ,", ",")
q = q.replace(" !", "!")
q = q.replace(" ?", "?")
q = q.replace(".", ". ")
q = q.replace(",", ", ")
q = q.replace("!", "! ")
q = q.replace("?", "? ")
q = q.replace("»", "")
q = q.replace("«", "")
q = q.replace("  ", " ")
print(q)

d = {}
e = []
s = list(q.split())  # за место line было f_in
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
        if slovo[-1] not in ".!?":
            print(slovo, end = " ")
        if j == (coun - 1):
            while slovo[-1] not in ".!?":
                slovo = random.choice(d.get(slovo))
            print(slovo, end = " ")
