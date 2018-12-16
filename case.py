"""Case-study #7 Генерация предложений
Разработчики:
Bayanova A., Shmatov D.

"""
import random


k = []
s = list(map(str, input().split()))
for i in range(len(s)):
    if s[i][0] == s[i][0].upper():
        k.append(s[i])

print(k)
