import re
s = input("Введите строку: ")
s = s.lower()
s = re.sub(r'[.,!?;:]', '', s) # посмотрела в инете как избавится от знаков препинания
words = s.split()
words = set(words)
print("Количество уникальных слов:", len(words))

maxLen = 0
for i in words:
    if len(i) >= maxLen:
        maxLen = len(i)
        maxW = i
print("Самое длинное слово:", maxW)

letters = list(s)
rez = dict()
for i in letters:
    if i == " ":
        continue
    kol = s.count(i)
    rez[i]= kol
print("Частота букв:", rez)