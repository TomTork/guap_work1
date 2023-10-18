# 19.  Ввести строку и букву,
# вывести только слова, начинающиеся с заданной буквы.


string_ = input().split()
letter_ = input()
print(*[i for i in string_ if i[0] == letter_])
