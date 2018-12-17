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
    if s[j-1] in d:
        m = "{} {}".format(d.get(s[j-1]), s[j])
        d.update({s[j-1] : m})
        if not s[j-1] in e:
            e.append(s[j-1])
    else:
        d.update({s[j-1] : s[j]})
for i in range(len(s)):
    if s[i][0] == s[i][0].upper():
        if not s[i][len(s[i])-1] == ".":
            first.append(s[i])
for i in range(len(s)):
    if s[i][len(s[i])-1] == ".":
        last.append(s[i])

print(first)  # выводит список первых слов

print(last)  # выводит список последних слов

print(e)  # выводит список слов не с одним значением ключа

print(d)  # выводит словарь


