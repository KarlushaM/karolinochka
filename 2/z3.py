import re

data = [
    "  Иван Иванов  ", 
    "Петров;Петр ", 
    "Сидорова Анна ", 
    "  ОЛЕГ КУЗНЕЦОВ  ", 
    "МАРИЯ; ТРОФИМОВА"
]
rez = []
for i in data:
    s = re.sub(r'[.,!?;:]', ' ', i)
    s = re.sub(r'\s+', ' ', s)
    s = s.strip()
    s = s.lower()
    s = s.title()
    rez.append(s)

# Ваще хз как подругому поменять ФИ местами, если компухтер сам не определит, что из этого имя
st1 = rez[1]
st2 = rez[2]
st1 = st1.split()
st2 = st2.split()
st1[0], st1[1] = st1[1], st1[0]
st2[0], st2[1] = st2[1], st2[0]
st11 = st1[0] + " " + st1[1]
st21 = st2[0] + " " + st2[1]
print(st11)
print(st21)

print("Отредактированные данные: ")
print(rez)