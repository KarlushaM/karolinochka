s = input("Введите строку: ")
s1=s.lower()
new_s = ""
for i in s1:
    if i == "а":
        new_s = new_s + "е"
    elif i == "е":
        new_s = new_s + "ё"
    elif i == "ё":
        new_s = new_s + "и"
    elif i == "и":
        new_s = new_s + "о"
    elif i == "о":
        new_s = new_s + "у"
    elif i == "у":
        new_s = new_s + "ы"
    elif i == "ы":
        new_s = new_s + "э"
    elif i == "э":
        new_s = new_s + "ю"
    elif i == "ю":
        new_s = new_s + "я"
    elif i == "я":
        new_s = new_s + "а"
    else:
        new_s = new_s + i
new_s = new_s.capitalize()
print("Новая строка: ", new_s)