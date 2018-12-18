"""Case-study #7 Генерация предложений
Разработчики:
Bayanova A., Shmatov D.

"""
import random

first = []
last = []

n = input()

n = n.replace("\n", " ")
n = n.replace("&", "")
n = n.replace("^", "")
n = n.replace("%", "")
n = n.replace("$", "")
n = n.replace("#", "")
n = n.replace("*", "")
n = n.replace("-", "")
n = n.replace("=", "")
n = n.replace("+", "")
n = n.replace("@", "")
n = n.replace(")", "")
n = n.replace("(", "")
n = n.replace("/", "")
n = n.replace(":", "")
n = n.replace(";", "")

n = n.replace(" .", ".")
n = n.replace(" ,", ",")
n = n.replace(" !", "!")
n = n.replace(" ?", "?")
n = n.replace(".", ". ")
n = n.replace(",", ", ")
n = n.replace("!", "! ")
n = n.replace("?", "? ")
n = n.replace("  ", " ")


d = {}
e = []
s = list(map(str, n.split()))
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


print(first)  # выводит список первых слов

print(last)  # выводит список последних слов

print(e)  # выводит список слов не с одним значением ключа

print(d)  # выводит словарь


