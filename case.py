"""Case-study #7 Генерация предложений
Разработчики:
Bayanova A., Shmatov D.

"""
import random
first = []
last = []

n = input()

def sp(n):
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
    n = n.replace(":", ": ")
    n = n.replace(",", ", ")
    n = n.replace("!", "! ")
    n = n.replace("?", "? ")
    n = n.replace("  ", " ")

sp(n)

s = list(map(str, n.split()))

for i in range(len(s)):
    if s[i][0] == s[i][0].upper():
        if not s[i][len(s[i])-1] == ".":
            first.append(s[i])

for i in range(len(s)):
    if s[i][len(s[i])-1] == ".":
        last.append(s[i])

print(last)
print(first)
