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
s = list(map(str, n.split()))
for j in range(1, len(s)):
    d.update({s[j-1] : s[j]})

for i in range(len(s)):
    if s[i][0] == s[i][0].upper():
        if not s[i][len(s[i])-1] == ".":
            first.append(s[i])

for i in range(len(s)):
    if s[i][len(s[i])-1] == ".":
        last.append(s[i])
print(d)
print(last)
print(first)
