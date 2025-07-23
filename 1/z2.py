s = []
for i in range(0, 1000000):
   n = input("Введите число ")
   try: 
     n = int(n)
     s.append(n)
   except:
      break
print("Последовательность чисел ", s)

print("Максимальное значение: ", max(s))
print("Минимальное значение: ", min(s))